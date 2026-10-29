# 📄 Fiche_Simple_-_Cloud_Dynatrace_OneAgent_Installer_Pilote_Linux.md

- **Environnement** : Dynatrace SaaS et hôte Linux administré
- **OS / Version** : Distribution et architecture prises en charge par OneAgent
- **Catégorie** : Observabilité / instrumentation

---

## 🎯 Problème précis à résoudre

Installer OneAgent sur un seul hôte pilote autorisé et confirmer sa visibilité dans le bon environnement Dynatrace.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Discovery & Coverage > Install > Install OneAgent**, choisir **Linux** et l'architecture exacte :
   ```bash
   uname -m
   ```
   👉 Explication : `x86_64` ou `aarch64` selon l'hôte.

2. Choisir le mode (**Infrastructure monitoring**, **Full-Stack** ou **Discovery**) et renseigner groupe d'hôtes et tags du pilote.
   👉 Explication : le groupe d'hôtes sert à étendre ensuite par lots.

3. Télécharger l'installateur depuis le tenant puis vérifier sa signature selon la commande fournie :
   ```bash
   wget --header="Authorization: Api-Token JETON_PAAS" -O Dynatrace-OneAgent.sh "https://ENVIRONNEMENT.live.dynatrace.com/api/v1/deployment/installer/agent/unix/default/latest?arch=x86"
   wget https://ca.dynatrace.com/dt-root.cert.pem
   ( echo 'Content-Type: multipart/signed; protocol="application/x-pkcs7-signature"; micalg="sha-256"; boundary="--SIGNED-INSTALLER"'; echo; echo; echo '----SIGNED-INSTALLER'; cat Dynatrace-OneAgent.sh ) | openssl cms -verify -CAfile dt-root.cert.pem > /dev/null
   ```
   👉 Explication : copier de préférence la commande exacte générée par la console (jeton et environnement inclus); « Verification successful » est attendu.

4. Installer avec privilèges élevés uniquement pour l'installation :
   ```bash
   sudo /bin/sh Dynatrace-OneAgent.sh --set-host-group=PILOTE
   ```
   👉 Explication : le mode non privilégié reste celui par défaut si la plateforme le permet.

5. Vérifier :
   ```bash
   systemctl status oneagent --no-pager
   ```
   👉 Explication : redémarrer les processus applicatifs seulement dans une fenêtre approuvée si l'instrumentation profonde l'exige.

## ⚡ 2. Production — Façon Simplifiée

1. Contrôler version et connexion : **Deployment Status > OneAgents** (dernière connexion, version, problèmes) et sur l'hôte :
   ```bash
   sudo /opt/dynatrace/oneagent/agent/tools/oneagentctl --get-server
   ```
   👉 Explication : étendre par groupe d'hôtes validés; mises à jour depuis la console ou l'outil d'automatisation approuvé.

## 🔒 3. Production — Façon Sécurisée

- Ne jamais publier les tokens d'installation, tenant tokens, URL de téléchargement ou commandes générées par le tenant; ils peuvent autoriser des téléchargements ou l'enrôlement.
- Autoriser uniquement les connexions sortantes nécessaires vers Dynatrace ou l'ActiveGate approuvé.
- Limiter l'accès aux journaux applicatifs et métadonnées à ce qui est justifié; évaluer l'injection automatique avec l'équipe applicative.
- Installer uniquement sur hôtes administrés et compatibles; ne pas forcer le contrôle de support OS pour contourner une incompatibilité.

## ✅ Validation et retour arrière

- **Validation** : signature validée, installation signalée comme réussie, hôte visible avec groupe/tags corrects et données attendues reçues.
- **Retour arrière** : désinstaller OneAgent par la procédure officielle de la version et confirmer la disparition du host après le délai prévu; documenter tout redémarrage nécessaire.

## 🔗 Si le problème n'est pas résolu

- [Dynatrace — Installer OneAgent sur Linux](https://docs.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-linux)
- [Dynatrace — Personnaliser l'installation Linux](https://docs.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux)