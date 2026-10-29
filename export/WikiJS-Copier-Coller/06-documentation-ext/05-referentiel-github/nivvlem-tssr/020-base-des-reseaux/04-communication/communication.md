# 📡 Module 04 – La communication réseau

## 🌍 Domaine de diffusion

- Un **domaine de diffusion** est un ensemble de machines pouvant recevoir des **diffusions broadcast**.
- Chaque **switch** forme un **unique domaine de broadcast**.
- Chaque **routeur** **sépare les domaines** de diffusion.

---

## 🔁 Communication réseau : théorie

### Communication dans le même réseau logique

- Deux machines ayant une **adresse IP dans le même sous-réseau** peuvent communiquer directement.
- Exemple : `192.168.1.10/24` peut pinger `192.168.1.20/24` → même réseau `192.168.1.0/24`

### Communication entre deux réseaux différents

- Si A et B sont sur des réseaux différents, il faut :
    - **Une passerelle par défaut** configurée sur chaque PC
    - Un **routeur** avec des routes vers les deux réseaux

### Exemple d’échange (avec ping)

1. La machine source fait une **requête ARP** pour connaître l’adresse MAC de la passerelle.
2. Elle envoie la **trame de ping au routeur**.
3. Le routeur **redirige** la trame selon sa **table de routage**.
4. La machine cible **répond au ping**, en suivant le même chemin à l’envers.

---

## 🧪 Démo Packet Tracer – Communication réseau

### Étapes dans Packet Tracer

1. **Add Simple PDU** → cliquer sur le PC source puis destination
2. Résultat affiché : **Succès ou échec**

### Mode simulation

- Active la **vue détaillée des couches OSI** pour chaque PDU
- Permet de suivre **l'encapsulation/désencapsulation**

### Exemples concrets

- Deux PCs sur même réseau (ex : 192.168.10.x /24) peuvent se pinguer sans routeur
- Deux PCs sur des réseaux différents (ex : 192.168.10.x /24 ↔ 192.168.20.x /24) nécessitent :
    - Des routeurs
    - Des **routes statiques** configurées sur les routeurs
    - Une **passerelle par défaut** sur les PCs

---

## 🚦 Notion de routage

- Le **routage** permet de transmettre les données entre **réseaux différents**
- Il s’effectue à la **couche 3 (réseau)** du modèle OSI
- Un **routeur** possède plusieurs interfaces réseau, chacune avec une IP propre

### Table de routage

- Liste des réseaux connus par le routeur
- Peut être **statique** (manuelle) ou **dynamique** (via protocoles comme OSPF, RIP…)

### Passerelle par défaut

- Adresse IP du **routeur** configurée sur les machines clientes
- Permet à un hôte de **sortir de son réseau**

---

## 🧠 Sur-réseau (supernetting)

### Définition

- Regrouper plusieurs sous-réseaux en **un seul sur-réseau**
- Avantages :
    - Moins de routes à gérer
    - Moins de ressources utilisées
    - Routage plus rapide

### Exemple

- Réseaux : 192.168.70.0/24, 192.168.100.128/25, 192.168.115.128/27
- Sur-réseau possible : **192.168.64.0 /18**

---

## 📘 À retenir pour les révisions

- Un ping ne fonctionne **entre réseaux différents** que si :
    - Une **passerelle est configurée**
    - Le **routeur connaît le réseau cible**
- Un routeur = plusieurs interfaces avec **IP distinctes**
- Le **routage** fonctionne à la **couche 3**
- Le **sur-réseau** permet d’agréger plusieurs réseaux logiques

## 🧑‍💼 Bonnes pratiques professionnelles

- Configurer systématiquement une **passerelle par défaut** sur les hôtes
- Documenter les **plages IP** et **routes statiques**
- Créer des **sur-réseaux** pour alléger les tables de routage
- Utiliser Packet Tracer pour tester des scénarios avant déploiement réel