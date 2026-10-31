import json
import sys
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pack_master as pm  # noqa: E402


class Handler(BaseHTTPRequestHandler):
    seen_headers = []

    def log_message(self, *a):
        pass

    def _send(self, body=b"x" * 100, code=200):
        Handler.seen_headers.append(dict(self.headers))
        self.send_response(code)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def do_HEAD(self):
        self.do_GET()

    def do_GET(self):
        if self.path == "/redir":
            self.send_response(302)
            self.send_header("Location", "/ok")
            self.send_header("Content-Length", "0")
            self.end_headers()
        elif self.path == "/redir-http":
            self.send_response(302)
            self.send_header("Location", "ftp://example.org/x")
            self.send_header("Content-Length", "0")
            self.end_headers()
        elif self.path == "/404":
            self._send(b"no", 404)
        elif self.path == "/big":
            self._send(b"y" * 5000)
        else:
            self._send()


class ProbeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.srv = HTTPServer(("127.0.0.1", 0), Handler)
        cls.base = f"http://127.0.0.1:{cls.srv.server_port}"
        threading.Thread(target=cls.srv.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.srv.shutdown()
        cls.srv.server_close()

    def probe(self, path, **kw):
        return pm.probe_url(self.base + path, allow_http=True, timeout=3, **kw)

    def test_head(self):
        r = self.probe("/ok")
        self.assertEqual((r["status"], r["length"], r["content_type"]), (200, 100, "text/html"))

    def test_get_counts_without_storing(self):
        r = self.probe("/ok", method="GET")
        self.assertEqual(r["length"], 100)
        self.assertNotIn("body", r)

    def test_redirect_final_url(self):
        r = self.probe("/redir")
        self.assertTrue(r["final_url"].endswith("/ok"))

    def test_bad_redirect_scheme_refused(self):
        self.assertIsNotNone(self.probe("/redir-http")["error"])

    def test_http_404(self):
        self.assertEqual(self.probe("/404")["status"], 404)

    def test_size_bound(self):
        r = self.probe("/big", method="GET", max_bytes=1000)
        self.assertTrue(r["truncated"])

    def test_http_refused_by_default(self):
        r = pm.probe_url(self.base + "/ok")
        self.assertIn("HTTPS", r["error"])

    def test_connection_error(self):
        r = pm.probe_url("http://127.0.0.1:1/", allow_http=True, timeout=1)
        self.assertIsNotNone(r["error"])

    def test_no_private_headers(self):
        Handler.seen_headers.clear()
        self.probe("/ok")
        keys = {k.lower() for k in Handler.seen_headers[-1]}
        self.assertFalse(keys & {"cookie", "authorization"})

    def test_method_restricted(self):
        with self.assertRaises(ValueError):
            pm.probe_url("https://example.org", method="POST")

    def test_cmd_sources_test_mode(self):
        with tempfile.TemporaryDirectory() as d:
            m = Path(d) / "m.json"
            m.write_text(json.dumps({"sources": [
                {"id": "a", "url": "https://example.org/"}]}))
            fake = {"url": "u", "status": 200, "final_url": "u",
                    "content_type": "t", "length": 1, "truncated": False, "error": None}
            with mock.patch.object(pm, "probe_url", return_value=fake):
                self.assertEqual(pm.cmd_sources(m, True, "HEAD", 1, 10), 0)
            fake["status"] = 500
            with mock.patch.object(pm, "probe_url", return_value=fake):
                self.assertEqual(pm.cmd_sources(m, True, "HEAD", 1, 10), 1)


class ManifestTests(unittest.TestCase):
    def write(self, data):
        d = tempfile.mkdtemp()
        p = Path(d) / "m.json"
        p.write_text(json.dumps(data))
        return p

    def test_default_manifest(self):
        s = pm.load_manifest(pm.DEFAULT_MANIFEST)
        self.assertEqual(len(s), 4)
        hosts = {pm.urllib.parse.urlsplit(x["url"]).hostname for x in s}
        self.assertEqual(hosts, {"github.com", "zentssr.com",
                                 "www.stephane-robert.info", "www.jousseaume.online"})

    def test_rejects_http(self):
        with self.assertRaises(ValueError):
            pm.load_manifest(self.write({"sources": [{"id": "a", "url": "http://x.org"}]}))

    def test_rejects_credentials_and_duplicates(self):
        with self.assertRaises(ValueError):
            pm.load_manifest(self.write({"sources": [{"id": "a", "url": "https://u:p@x.org"}]}))
        with self.assertRaises(ValueError):
            pm.load_manifest(self.write({"sources": [
                {"id": "a", "url": "https://x.org"}, {"id": "a", "url": "https://y.org"}]}))

    def test_list_mode_no_network(self):
        with mock.patch.object(pm, "probe_url", side_effect=AssertionError):
            self.assertEqual(pm.cmd_sources(pm.DEFAULT_MANIFEST, False, "HEAD", 1, 1), 0)


class RootAndRunTests(unittest.TestCase):
    def test_find_root(self):
        self.assertTrue((pm.find_root() / pm.MARKER).is_file())

    def test_find_root_missing(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(FileNotFoundError):
                pm.find_root(Path(d))

    def test_check_and_refresh_steps(self):
        calls = []
        with mock.patch.object(pm, "run_script", side_effect=lambda r, s, *a: calls.append((s, a)) or 0):
            self.assertEqual(pm.cmd_check(Path("/r")), 0)
            self.assertEqual(calls, [
                ("verify_wiki.py", ()),
                ("03-Qualite-Tests/check_links.py", ()),
            ])
            calls.clear()
            self.assertEqual(pm.cmd_refresh(Path("/r")), 0)
            self.assertEqual(calls[1][1], ("--refresh",))
            self.assertEqual(calls[-1][1], ("--check", "--manual"))

    def test_stops_on_failure(self):
        with mock.patch.object(pm, "run_script", return_value=3) as m:
            self.assertEqual(pm.cmd_check(Path("/r")), 3)
            self.assertEqual(m.call_count, 1)

    def test_all_skips_sources_on_check_failure(self):
        with mock.patch.object(pm, "cmd_check", return_value=1), \
             mock.patch.object(pm, "cmd_sources") as s:
            self.assertEqual(pm.main(["all"]), 1)
            s.assert_not_called()

    def test_all_checks_before_sources_without_export_refresh(self):
        with mock.patch.object(pm, "cmd_check", return_value=0) as check, \
             mock.patch.object(pm, "cmd_sources", return_value=0) as sources:
            self.assertEqual(pm.main(["all"]), 0)
            check.assert_called_once()
            sources.assert_called_once()


if __name__ == "__main__":
    unittest.main()
