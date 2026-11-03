---
title: "Lecture seule : relève les infos de la machine locale et écrit une fiche machine pré-remplie."
description: "set -u"
published: true
date: 2026-11-03T14:22:29Z
tags: ["fiche-machine", "type", "id-linux"]
editor: markdown
dateCreated: 2026-11-03T14:22:29Z
dateModified: 2026-11-03T14:22:29Z
---

#!/usr/bin/env bash
# Lecture seule : relève les infos de la machine locale et écrit une fiche machine pré-remplie.
# Les champs non détectables restent « [à compléter] ».
# Usage : ./collecter-machine.sh [fichier_sortie.md]   (sudo conseillé pour les ports et le pare-feu)
set -u

TODO="[à compléter]"
HOST="$(hostname 2>/dev/null | cut -d. -f1)"; HOST="${HOST:-$(cat /etc/hostname 2>/dev/null)}"
OUT="${1:-fiche-machine_${HOST}.md}"

. /etc/os-release 2>/dev/null
virt="$(systemd-detect-virt 2>/dev/null)"
case "$virt" in
  lxc|lxc-libvirt|openvz) type="[[Glossary:LXC]]" ;;
  none|"") type="Physique" ;;
  *) type="[[Glossary:VM]] ($virt)" ;;
esac

ips="$(ip -o -4 addr show scope global 2>/dev/null | awk '{print $2": "$4}' | paste -sd', ' -)"
disks="$(df -h --output=target,size,fstype -x tmpfs -x devtmpfs -x squashfs 2>/dev/null | tail -n +2 | awk '{print $1" "$2" ("$3")"}' | paste -sd', ' -)"
services="$(systemctl list-units --type=service --state=running --no-legend 2>/dev/null | awk '{print $1}' | sed 's/\.service$//' | paste -sd', ' -)"
ports="$(ss -H -tuln 2>/dev/null | awk '{n=split($5,a,":"); print tolower($1)"/"a[n]}' | sort -u | paste -sd', ' -)"

if command -v nft >/dev/null && nft list ruleset 2>/dev/null | grep -q .; then
  fw="nftables actif"
elif command -v ufw >/dev/null && ufw status 2>/dev/null | grep -q "Status: active"; then
  fw="ufw actif"
elif command -v iptables >/dev/null && [ "$(iptables -S 2>/dev/null | wc -l)" -gt 3 ]; then
  fw="iptables actif"
else
  fw="aucun pare-feu détecté (ou droits insuffisants)"
fi

today="$(date +%F)"
cat > "$OUT" <<EOF
# 📄 ${TODO}_${HOST}_${ID:-linux}-${VERSION_ID:-}

- **Tags** : \`fiche-machine\`, \`${type%% *}\`, \`${ID:-linux}\`

---

### 📌 1. Identification & Métadonnées
* **Machine Physique / Hôte** : ${TODO}
* **Environnement** : ${TODO}
* **Type d'équipement** : ${type}
* **Nom de la Machine** : ${HOST}
* **Système d'Exploitation (OS)** : ${PRETTY_NAME:-$(uname -s)} (noyau $(uname -r))
* **Statut Opérationnel** : ${TODO}

---

### 📋 2. Rôle, Utilisation & Besoins (Ressources)
* **Rôle et Utilisation** : ${TODO}
* **Besoins (Allocation ressources)** :
  * **vCPU** : $(nproc)
  * **[[Glossary:RAM]]** : $(free -h | awk '/^Mem:/{print $2}')
  * **Stockage** : ${disks:-$TODO}
  * **Adresse [[Glossary:IP]]** : ${ips:-$TODO}

---

### 📦 3. Logiciels & Ports
* **Logiciels installés** : ${services:-$TODO}
* **Ports ouverts** : ${ports:-$TODO}

---

### 🛡️ 4. Sécurité & Pare-feu
* **Firewall Machine (local)** : ${fw}
* **Firewall Externe (Hôte / Routeur)** : ${TODO}

---

### 📅 6. Suivi des Dates & Historique
- **Date de création** : ${TODO}
- **Dernière modification** : ${today}
- **Historique des modifications datées** :
  - \`${today}\` : relevé automatique par collecter-machine.sh
EOF
echo "Fiche écrite : $OUT"