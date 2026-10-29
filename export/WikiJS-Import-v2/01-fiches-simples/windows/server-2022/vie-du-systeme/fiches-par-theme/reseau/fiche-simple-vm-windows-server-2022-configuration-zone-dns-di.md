---
title: "VM_WinSrv_2022_DNS_Configuration-Zone-Directe-Inverse"
description: "Installer le rôle Serveur DNS sur Windows Server 2022, créer une zone de recherche directe (lab.local), une zone de recherche inversée (1.168.192.in-addr.arpa), ajouter des enregistrements de type A et PTR, et sécuriser le service DNS contre le cache poisoning et les transferts de zone non autorisés"
published: true
date: 2026-10-29T20:22:42Z
tags: ["[windows-server-2022]", "[windows-family]", "[dns]", "[zone-directe]", "[zone-inverse]", "[gui]", "[powershell]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 VM_WinSrv_2022_DNS_Configuration-Zone-Directe-Inverse.md

- **Environnement** : VM (Hyper-V / Proxmox VE / VSphere)
- **OS / Version** : Windows Server 2022 Standard / Datacenter - Famille Windows
- **Catégorie** : Services Réseau / DNS
- **Tags** : `[windows-server-2022]`, `[windows-family]`, `[dns]`, `[zone-directe]`, `[zone-inverse]`, `[gui]`, `[powershell]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer le rôle Serveur DNS sur Windows Server 2022, créer une zone de recherche directe (`lab.local`), une zone de recherche inversée (`1.168.192.in-addr.arpa`), ajouter des enregistrements de type A et PTR, et sécuriser le service DNS contre le cache poisoning et les transferts de zone non autorisés.

---

## 🖥️ Méthode Interface Graphique (GUI pas-à-pas)

### Prérequis
- Configurer une adresse IP statique sur le serveur et confirmer le plan DNS avec l'administrateur réseau.
- Choisir le type de zone avant création : une zone intégrée AD est réservée à un serveur DNS hébergé sur un contrôleur de domaine ; une zone autonome est stockée dans un fichier.
- Une mise à jour dynamique sécurisée n'est disponible que pour une zone intégrée à Active Directory.

### Installer le rôle DNS
1. Dans **Gestionnaire de serveur** > **Gérer** > **Ajouter des rôles et fonctionnalités**, choisir **Installation basée sur un rôle ou une fonctionnalité**, sélectionner le serveur local, puis cocher **Serveur DNS**.
2. Accepter les outils d'administration proposés, poursuivre l'assistant et sélectionner **Installer**. Vérifier la réussite dans **Résultats**.
3. Ouvrir **Gestionnaire de serveur** > **Outils** > **DNS** (ou `dnsmgmt.msc`).

### Créer la zone directe et la zone inverse
1. Dans DNS Manager, clic droit sur **Zones de recherche directe** > **Nouvelle zone...**. Choisir **Zone principale**. Si le serveur est un DC et que la zone appartient au domaine AD, choisir **Stocker la zone dans Active Directory** et le périmètre de réplication validé ; sinon conserver une zone principale fichier.
2. Saisir le nom de zone (`lab.local` uniquement si ce suffixe est réellement celui de l'environnement). Pour une zone AD intégrée, choisir **Mises à jour dynamiques sécurisées uniquement**. Ne pas activer les mises à jour non sécurisées.
3. Clic droit sur **Zones de recherche inversée** > **Nouvelle zone...**. Choisir **Zone principale**, le mode de stockage cohérent avec la zone directe, **IPv4**, puis l'ID réseau `192.168.1` pour le sous-réseau `192.168.1.0/24`. Configurer les mises à jour dynamiques de la même façon que pour la zone directe.
4. Ajouter les enregistrements A/PTR avec la procédure GUI de la fiche [DNS — créer un enregistrement A et CNAME](/01-fiches-simples/windows/server-2022/vie-du-systeme/fiches-par-theme/reseau/fiche-simple-vm-windows-server-2022-dns-creer-enregistrement). Cocher la création PTR associée seulement si la zone inverse existe et si le serveur est autorisé à la modifier.

### Sécuriser et vérifier
1. Dans les propriétés de chaque zone, onglet **Transferts de zone**, désactiver les transferts s'ils ne sont pas nécessaires ; sinon les limiter aux serveurs DNS secondaires approuvés. Ne jamais autoriser le transfert à n'importe quel serveur.
2. Dans les propriétés du serveur > **Redirecteurs**, saisir uniquement les résolveurs amont approuvés par l'organisation. Ne pas utiliser directement des DNS publics pour un domaine AD interne sans décision d'architecture.
3. Vérifier que les zones et enregistrements apparaissent dans DNS Manager, puis tester les résolutions directe et inverse depuis un client autorisé. Une vérification CLI `nslookup` peut compléter le contrôle graphique.

Référence : [Microsoft Learn — Installer et configurer DNS Server](https://learn.microsoft.com/en-us/windows-server/networking/dns/quickstart-install-configure-dns-server).

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation rapide du rôle DNS sans outils d'administration graphiques :
   `Install-WindowsFeature -Name DNS`
   👉 Explication : Installe le service DNS de base sur le serveur Windows local.

2. Création d'une zone directe principale non intégrée à Active Directory :
   `Add-DnsServerPrimaryZone -Name "lab.local" -ZoneFile "lab.local.dns"`
   👉 Explication : Crée la zone de résolution directe lab.local stockée dans un fichier texte standard.

3. Ajout d'un enregistrement hôte (A) de test :
   `Add-DnsServerResourceRecordA -Name "srv-test" -ZoneName "lab.local" -IPv4Address "192.168.1.50"`
   👉 Explication : Associe le nom srv-test.lab.local à l'adresse IP 192.168.1.50.

4. Test de résolution locale :
   `Resolve-DnsName -Name "srv-test.lab.local" -Server "127.0.0.1"`
   👉 Explication : Interroge directement le serveur DNS local pour valider la résolution de nom.

---

## ⚡ 2. Production — Façon Simplifiée
1. Installation du rôle DNS avec les consoles d'administration RSAT :
   `Install-WindowsFeature -Name DNS -IncludeManagementTools`
   👉 Explication : Installe le service DNS ainsi que la console graphique `dnsmgmt.msc` et les modules PowerShell.

2. Création de la zone directe principale intégrée Active Directory :
   `Add-DnsServerPrimaryZone -Name "lab.local" -ReplicationScope "Forest"`
   👉 Explication : Crée la zone directe et la réplique automatiquement sur tous les contrôleurs de domaine de la forêt.

3. Création de la zone de recherche inversée intégrée Active Directory :
   `Add-DnsServerPrimaryZone -NetworkId "192.168.1.0/24" -ReplicationScope "Forest"`
   👉 Explication : Crée la zone inversée 1.168.192.in-addr.arpa pour convertir les IP en noms FQDN.

4. Création simultanée d'un enregistrement A et de son pointeur PTR :
   `Add-DnsServerResourceRecordA -Name "srv-app" -ZoneName "lab.local" -IPv4Address "192.168.1.60" -CreatePtr`
   👉 Explication : Crée à la fois l'enregistrement srv-app.lab.local -> 192.168.1.60 et le pointeur PTR 192.168.1.60 -> srv-app.lab.local.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Restriction des mises à jour dynamiques aux seuls hôtes authentifiés AD :
   `Set-DnsServerPrimaryZone -Name "lab.local" -DynamicUpdate Secure`
   👉 Explication : Bloque l'injection d'enregistrements DNS par des machines non jointes au domaine Active Directory.

2. Interdiction stricte des transferts de zone DNS non autorisés :
   `Set-DnsServerPrimaryZone -Name "lab.local" -SecureSecondaries NoTransfer`
   👉 Explication : Empêche les attaquants de télécharger l'intégralité de la cartographie DNS du réseau.

3. Activation du verrouillage du cache DNS (Cache Locking) et anti-recul :
   `Set-DnsServerCache -CacheLockingPercent 96`
   👉 Explication : Empêche la modification des enregistrements en cache jusqu'à l'expiration de leur TTL (protection contre le Cache Poisoning / Spoofing).

4. Configuration des réexpéditeurs DNS approuvés :
   `Set-DnsServerForwarder -IPAddress "10.0.0.53","10.0.0.54"`
   👉 Explication : Le cmdlet `Set-DnsServerForwarder` configure des adresses de transfert ; il n'active pas DoH/DoT et ne possède pas de paramètre `-UseSPIFT`. Remplacer les adresses d'exemple par les résolveurs amont approuvés. Un transport DNS chiffré nécessite un composant compatible distinct.

5. Application des règles de pare-feu Windows pour le trafic DNS sécurisé :
   `Set-NetFirewallRule -DisplayGroup "Serveur DNS" -Enabled True -Profile Domain,Private`
   👉 Explication : Autorise les flux UDP/TCP 53 uniquement sur les profils réseau privés et de domaine.