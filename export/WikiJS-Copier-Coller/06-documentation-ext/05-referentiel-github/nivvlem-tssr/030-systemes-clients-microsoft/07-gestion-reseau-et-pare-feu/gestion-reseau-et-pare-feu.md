# La gestion du réseau et du pare-feu

## 🚀 Rappel sur les bases réseau (ARP, routage)

- Chaque machine dispose d'une **adresse IP** et d'une **adresse MAC**.
- Le **cache ARP** est utilisé pour associer une IP à une MAC connue.
- Les **routeurs** utilisent leur **table de routage** pour déterminer où acheminer un paquet IP.

### Exemple de cheminement IP :

- Si une machine A veut joindre B située sur un autre réseau,
    - Elle envoie le paquet vers sa **passerelle par défaut** (routeur)
    - Le routeur consulte sa **table de routage**
    - Il transmet le paquet via la bonne interface après avoir résolu l'adresse MAC cible via **ARP**

> 🔹 Une bonne connaissance du modèle OSI et de l'encapsulation (couche 2/couche 3) est indispensable.

---

## 🛠️ Configuration de la carte réseau

### 📂 Emplacement réseau

- Un poste Windows classe le réseau comme :
    - **Privé** : découverte réseau autorisée
    - **Public** : plus restrictif (pare-feu plus strict)
    - **Domaine** : si le poste est joint à un domaine Active Directory

### 🔧 Paramètres à configurer

- Adresse IP + masque de sous-réseau
- Passerelle par défaut
- Serveurs DNS (préféré + auxiliaire)
- Mode d'attribution :
    - **Statique** (manuelle)
    - **Dynamique** (DHCP)
    - **APIPA** : 169.254.x.x si aucun DHCP n'est joignable

### 🔢 Outils graphiques

- Icône réseau > Centre réseau et partage
- `ncpa.cpl` : accès direct aux connexions réseau

### 💪 Outils en ligne de commande

|Commande|Description|
|---|---|
|`ipconfig`|Affiche la config IP, renouvelle le bail DHCP|
|`ping`|Test de connectivité (ICMP, bloqué parfois)|
|`tracert`|Affiche les sauts d'un paquet IP|
|`nslookup`|Diagnostic de la résolution DNS|

---

## 🔒 Pare-feu Windows

### 🌀 Rôle

- Contrôle les flux **entrant/sortant** autorisés
- S'adapte à l'**emplacement réseau** du poste
- Définit une stratégie de sécurité cohérente

### 🔧 Niveaux d'administration

|Mode|Accès|
|---|---|
|**Basique**|`firewall.cpl` (activer/désactiver)|
|**Programmes autorisés**|"Autoriser une application via le pare-feu"|
|**Avancé (pro)**|Pare-feu Defender avec fonctions avancées (`wf.msc`)|

### 🔹 Caractéristiques

- **Activé par défaut**
- Bloque les flux entrants (sauf règle explicite)
- Autorise les flux sortants
- Peut être géré par **GPO** ou **via PowerShell**

---

## ✅ À retenir pour les révisions

- Une carte réseau est liée à un emplacement : privé, public ou domaine
- Les outils en ligne de commande offrent un meilleur contrôle pour le diagnostic
- Le pare-feu Windows bloque par défaut les connexions entrantes
- Le mode avancé `wf.msc` permet de créer des règles sur-mesure
- Toujours vérifier les profils réseaux affectés aux interfaces !

---

## 📌 Bonnes pratiques professionnelles

|Pratique|Pourquoi ?|
|---|---|
|Documenter l'adresse IP, masque, passerelle|Traçabilité et dépannage plus simple|
|Utiliser DHCP avec baux réservés si possible|Centralisation, gain de temps|
|Réduire les privilèges pour les utilisateurs|Éviter la désactivation intempestive du pare-feu|
|Bloquer par défaut, autoriser par exception|Principe du moindre privilège en sécurité|
|Exporter la conf pare-feu dans les scripts GPO|Déploiement uniforme dans les réseaux d'entreprise|