# L’adressage IPv4

## 🧱 Structure d’une adresse IPv4

- Une adresse IPv4 = **32 bits** divisés en **4 octets**
- Composée de deux parties :
    - **ID_Réseau** : identifie le réseau logique
    - **ID_Hôtes** : identifie les machines dans le réseau
- Pour fonctionner, un hôte a besoin de :
    - Une **adresse IP**
    - Un **masque de sous-réseau**

---

## 🏷️ Les classes IPv4 (RFC 790)

|Classe|Plage du 1er octet|Masque par défaut|Hôtes max|
|---|---|---|---|
|A|1 – 126|255.0.0.0 (/8)|16 777 214|
|B|128 – 191|255.255.0.0 (/16)|65 534|
|C|192 – 223|255.255.255.0 (/24)|254|
|D|224 – 239|Multicast|Non applicable|

📌 Les adresses en **127.x.x.x** sont réservées à la **boucle locale** (loopback).

---

## 🧾 Types d’adresses IPv4

- **Adresse réseau** : bits d’ID_Hôtes = 0
- **Adresse de diffusion (broadcast)** : bits d’ID_Hôtes = 1
- **Adresse d’hôte** : mélange de 0 et 1 dans la partie hôte

### Exemple

- IP : 192.168.1.0 avec masque 255.255.255.0 → adresse réseau
- IP : 192.168.1.255 avec masque 255.255.255.0 → diffusion
- IP : 192.168.1.100 avec masque 255.255.255.0 → hôte

---

## 🧮 La notation CIDR (Classless Inter Domain Routing)

### Présentation

- Notation simplifiée : **192.168.10.1 /24** au lieu de 255.255.255.0
- Le **/24** indique **24 bits à 1** dans le masque de sous-réseau

### Conversion CIDR ↔ Standard

- /20 → 255.255.240.0
- /23 → 255.255.254.0
- /30 → 255.255.255.252

### Conversion Standard ↔ CIDR

- Compter les bits à 1 dans le masque binaire
    - Exemple : 255.255.248.0 → /21

---

## 🔢 Calculs d’adresses réseau

### Adresse de réseau

- Appliquer un **ET logique (&)** entre l’IP et le masque de sous-réseau
- Tous les bits de la partie hôte deviennent **0**

### Adresse de diffusion (broadcast)

- Même logique, mais tous les bits de la partie hôte deviennent **1**

### Nombre d’hôtes possibles

- Formule : **2ⁿ – 2** (n = nb de bits pour les hôtes)

---

## 🧩 Création et découpage en sous-réseaux

### Étapes

1. Déterminer le **nombre de sous-réseaux** souhaités
2. Convertir ce nombre en **binaire** pour déterminer les **bits nécessaires**
3. Ajouter ces bits à la **CIDR de base**
4. Générer les **adresses de sous-réseaux** via l'incrémentation binaire

### Exemple :

- Réseau : 192.168.10.0 /24, 8 sous-réseaux → 3 bits → /27 → 255.255.255.224
- Incrément : 32
- Résultats : 192.168.10.0, .32, .64, .96, .128, .160, .192, .224

---

## 🏠 Adresses spéciales IPv4

### Adresses privées (RFC 1918)

|Classe|Plage|CIDR par défaut|
|---|---|---|
|A|10.0.0.0 – 10.255.255.255|/8|
|B|172.16.0.0 – 172.31.255.255|/12|
|C|192.168.0.0 – 192.168.255.255|/16|

### Adresses APIPA (RFC 3927)

- Plage : 169.254.0.0 /16
- Affectation automatique en **absence de DHCP**
- Non routables sur Internet

---

## 📘 À retenir pour les révisions

- Une adresse IPv4 = 32 bits → 4 octets
- Connaître les **classes** et leurs plages
- Savoir convertir entre **notation standard et CIDR**
- Maîtriser les types d’adresses : **réseau, hôte, broadcast**
- Calculer le **nombre d’hôtes** et les **sous-réseaux**

## 🧑‍💼 Bonnes pratiques professionnelles

- Utiliser les **adresses privées** pour les réseaux internes
- Segmenter via **sous-réseaux bien pensés** (limiter le broadcast)
- Éviter les chevauchements d’adresses avec **une planification IP claire**
- Utiliser les **notations CIDR** dans les configurations pro (pare-feu, routeurs…)