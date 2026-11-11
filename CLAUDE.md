# EPG auto-hébergé pour Kodi

Remplace un EPG payant pour Kodi (PVR IPTV Simple Client). Tourne sous Docker Desktop (Mac), en local.
Données visées au minimum : titre, image, résumé long (en français si possible).

## Architecture

| Dossier | Rôle | URL |
|---|---|---|
| `xmltvfr/` | **guide final pour Kodi** : filtre le XMLTV complet de xmltvfr.fr sur `channels.txt`, puis fusionne le guide iptv-org | `http://<ip-du-mac>:8082/guide.xml.gz` |
| `iptv-org/` | grab des chaînes absentes de xmltvfr (`public/channels.xml`), 3 fois par jour | `:8081` (sortie intermédiaire) |
| `webgrabplus/` | alternative WebGrab+Plus, gardée pour comparaison seulement | `:8080` |

- Les stacks `xmltvfr/` et `iptv-org/` doivent tourner toutes les deux. Si iptv-org est arrêté, le guide ne contient que les chaînes xmltvfr.
- `xmltvfr/app/filter.py` : en cas de doublon d'id, xmltvfr est prioritaire. Le script recopie aussi `<image>` en `<icon>`.
- `CHANNELS.md` : correspondance entre les 113 chaînes de l'utilisateur (id interne) et leur `tvg-id`, leur source et la qualité mesurée.
- Dans la playlist M3U, le `tvg-id` doit être exactement l'id XMLTV.

## Ajouter ou retirer une chaîne

1. Chercher d'abord dans xmltvfr.fr (<https://xmltvfr.fr/channels.php>) : données riches, en français. L'ajouter dans `xmltvfr/channels.txt`.
2. Sinon, chercher dans `iptv-org/epg/sites/*/*.channels.xml` et l'ajouter dans `iptv-org/public/channels.xml` avec un `xmltv_id` unique.
3. Tester une source avant de l'ajouter :
   ```sh
   cd iptv-org && docker compose run --rm -e RUN_AT_STARTUP=false iptv-org-epg \
     npm run grab -- --channels=public/test-channels.xml --output=public/test.xml --days=1
   ```
4. `docker compose restart` dans `iptv-org/`, puis dans `xmltvfr/`. Mettre à jour `CHANNELS.md`.

## Pièges vérifiés (11/11/2026)

- **Kodi ne lit que `<icon src>`** pour la vignette d'un programme, pas `<image>` (pvr.iptvsimple, `EpgEntry.cpp`).
- **WebGrab+Plus gratuit est inutilisable pour ce besoin.** Les licences `default` et `registered` ne donnent ni images ni lecture des siteini chiffrés V3 (dont programme-tv.net). Il faut la licence donateur (~6 €).
- **Docker Desktop (moteur 20.10) ne relaie pas l'ICMP.** Le « Checking Internet » de WebGrab+Plus échoue donc : il est contourné par `webgrabplus/scripts/ping-http.sh`, monté sur `/bin/ping`.
- **Image linuxserver/webgrabplus** : on ne peut pas monter un fichier seul sur `/etc/crontabs/abc` (« Resource busy ») : il faut monter le dossier `crontabs/`.
- **Sources iptv-org** :
  - en panne : pickx.be (403 anti-robot), chaines-tv.orange.fr (0 programme) ;
  - tv.sfr.fr n'a plus Sat.1 ;
  - tv.blue.ch est la meilleure source pour les chaînes DE et IT ;
  - epgshare01.online ne donne que le titre et le résumé.

  Ces sources changent souvent : les revérifier avant de les recommander.
