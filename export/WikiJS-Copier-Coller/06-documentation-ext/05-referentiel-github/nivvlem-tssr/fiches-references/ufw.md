# UFW (Uncomplicated Firewall)

## 📌 Présentation

`ufw` est une interface simplifiée pour gérer les règles du pare-feu `iptables`, principalement sur les distributions Ubuntu et Debian. Il permet de sécuriser un serveur en limitant les ports ouverts avec une syntaxe simple et intuitive.

---

## ✅ Activation & statut

```bash
sudo ufw enable        # Active le pare-feu
sudo ufw disable       # Désactive le pare-feu
sudo ufw status verbose  # Affiche les règles actuelles
```

---

## 🧰 Commandes essentielles

| Commande | Description | Exemple |
|----------|-------------|---------|
| `ufw allow` | Autorise une connexion | `sudo ufw allow 22` |
| `ufw allow from IP` | Autorise une IP spécifique | `sudo ufw allow from 192.168.1.100` |
| `ufw deny` | Bloque un port | `sudo ufw deny 21` |
| `ufw delete` | Supprime une règle | `sudo ufw delete allow 22` |
| `ufw reset` | Réinitialise toutes les règles | `sudo ufw reset` |
| `ufw default` | Définit la politique par défaut | `sudo ufw default deny incoming` |

---

## 🔒 Services préconfigurés

UFW peut utiliser des noms de services définis dans `/etc/services` :

```bash
sudo ufw allow ssh
sudo ufw allow "Apache Full"
```

---

## 🔎 Cas d’usage courant

- Ouvrir uniquement les ports nécessaires sur un serveur Linux
- Restreindre les connexions SSH à une IP ou un sous-réseau
- Bloquer temporairement un port ou un service
- Visualiser rapidement les règles de pare-feu actives

---

## ⚠️ Erreurs fréquentes

- Oublier d’autoriser le port SSH avant `ufw enable` → perte d’accès
- Laisser le pare-feu désactivé en production
- Ne pas tester les règles sur une VM locale avant de les appliquer à un serveur distant

---

## ✅ Bonnes pratiques

- Toujours commencer par `ufw allow OpenSSH` ou `22` avant activation
- Définir les politiques par défaut :
  ```bash
  sudo ufw default deny incoming
  sudo ufw default allow outgoing
  ```
- Éviter les règles trop larges (ex : `ufw allow from any`)
- Utiliser des règles explicites avec IP + port si possible

---

## 📚 Ressources complémentaires

- `man ufw`, `ufw --help`
- [Guide Ubuntu UFW](https://help.ubuntu.com/community/UFW)
- [DigitalOcean – How To Set Up a Firewall with UFW](https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands)