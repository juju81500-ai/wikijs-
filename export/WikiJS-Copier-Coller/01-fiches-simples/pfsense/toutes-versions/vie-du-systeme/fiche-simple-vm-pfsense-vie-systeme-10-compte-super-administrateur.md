# Fiche_Simple_-_VM_pfSense_Vie_Systeme_10_Compte_Super_Administrateur

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 10 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Sécuriser le compte `admin`, créé avec le mot de passe par défaut `pfsense`.

## 1. Hors-Production (Lab / Test / POC)

1. Changer le mot de passe dans l'assistant (étape « Set Admin WebGUI Password ») ou System > User Manager > admin > Edit > Password.
   👉 Explication : le mot de passe par défaut est public; le changer évite toute prise de contrôle.

2. Ou en console (option 3 « Reset webConfigurator password »), ou en shell :
   ```sh
   pfSsh.php playback changepassword admin
   ```
   👉 Explication : demande le nouveau mot de passe de `admin` sans passer par l'interface web.

3. Contrôler les comptes d'UID 0 :
   ```sh
   awk -F: '$3==0{print $1}' /etc/passwd
   ```
   👉 Explication : seuls `root` (et `admin` mappé) doivent apparaître.

## 2. Production — Contrôles

Stocker le mot de passe dans un coffre-fort et le réserver aux urgences.

## 3. Production — Sécurité

Mot de passe long et unique; activer le 2FA (System > User Manager > Authentication Servers, TOTP).

## Validation et retour arrière

- **Validation** : Le mot de passe par défaut est refusé.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire pfSense CE](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-pfsense)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)