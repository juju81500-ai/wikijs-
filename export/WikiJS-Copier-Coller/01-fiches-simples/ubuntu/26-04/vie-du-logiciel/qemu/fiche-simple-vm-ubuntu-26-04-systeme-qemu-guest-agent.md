# 📄 Fiche_Simple_-_VM_Ubuntu_26.04_Systeme_Qemu_Guest_Agent

- **Environnement** : VM Ubuntu sur hyperviseur KVM/QEMU (Proxmox VE, libvirt, OpenStack)
- **OS / Version** : Ubuntu Server 26.04 LTS
- **Catégorie** : Système / Virtualisation / Agent invité

---

## 🎯 Problème précis à résoudre

Installer l'agent invité QEMU sur une VM Ubuntu 26.04 pour que l'hyperviseur reçoive l'adresse IP, l'état du système et permette un arrêt propre ou une sauvegarde cohérente du système de fichiers.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Vérifier que la VM est bien virtualisée par QEMU/KVM :
```bash
systemd-detect-virt
```
👉 Explication : Retourne `kvm` ou `qemu` lorsque la machine tourne sur un hyperviseur QEMU. La commande fait partie du paquet systemd déjà installé sur Ubuntu 26.04. Un autre résultat (par exemple `vmware`) signale qu'il ne faut pas installer cet agent.

2. Installer l'agent :
```bash
sudo apt update
sudo apt install -y qemu-guest-agent
```
👉 Explication : Installe le démon `qemu-guest-agent` qui communique avec l'hyperviseur via le canal virtio-serial.

3. Vérifier que le service tourne :
```bash
sudo systemctl enable --now qemu-guest-agent
systemctl status qemu-guest-agent --no-pager
```
👉 Explication : Active le démarrage automatique et lance immédiatement le service. Le statut doit afficher `active (running)`.

## ⚡ 2. Production — Façon Simplifiée

1. Activer l'option agent côté hyperviseur (Proxmox : VM > Options > QEMU Guest Agent) puis redémarrer la VM.
👉 Explication : Sans l'option côté hyperviseur, le canal virtio-serial n'existe pas et l'agent reste inactif, même installé dans la VM.

2. Vérifier la remontée d'informations depuis l'hyperviseur :
```bash
sudo ip -br address
```
👉 Explication : Les adresses listées ici doivent aussi apparaître dans l'interface de l'hyperviseur. Côté Proxmox, la commande `qm agent <VMID> network-get-interfaces` (exécutée sur l'hôte) doit répondre.

## 🔒 3. Production — Façon Sécurisée

1. Vérifier le périphérique de canal exposé à la VM :
```bash
ls -l /dev/virtio-ports/
```
👉 Explication : Le port `org.qemu.guest_agent.0` doit être présent. Son absence indique une configuration matérielle VM incomplète.

2. Limiter les commandes autorisées par l'agent :
```bash
sudo nano /etc/default/qemu-guest-agent
```
Exemple de contenu :
```text
BLACKLIST_RPC=guest-file-read,guest-file-write,guest-file-open,guest-exec,guest-set-user-password
```
👉 Explication : Ces RPC permettent à l'hyperviseur d'accéder aux fichiers ou d'exécuter des commandes dans la VM. Les désactiver réduit la surface d'attaque si l'hôte est compromis ; ne les bloquer que si les procédures d'exploitation ne les utilisent pas.

3. Redémarrer l'agent après modification :
```bash
sudo systemctl restart qemu-guest-agent
```
👉 Explication : Recharge la liste `BLACKLIST_RPC` ; sans redémarrage, l'ancienne configuration reste active.

## ✅ Validation et retour arrière

- **Précontrôles** : confirmer `systemd-detect-virt` ; sauvegarder ou snapshoter la VM avant l'option côté hyperviseur.
- **Validation** : `systemctl is-active qemu-guest-agent` renvoie `active` ; l'hyperviseur affiche l'adresse IP de la VM.
- **Retour arrière** : désactiver l'option agent dans l'hyperviseur, puis `sudo systemctl disable --now qemu-guest-agent`.