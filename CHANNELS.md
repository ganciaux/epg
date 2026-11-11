# Correspondance des chaînes EPG

Guide final pour Kodi : **`http://<ip-du-mac>:8082/guide.xml.gz`** (dossier [`xmltvfr/`](xmltvfr/)).

Il fusionne deux sources :

| Source | Fichier de config | Rôle |
|---|---|---|
| [xmltvfr.fr](https://xmltvfr.fr) | [`xmltvfr/channels.txt`](xmltvfr/channels.txt) | prioritaire : FR / BE / principales DE, données riches, textes en français |
| [iptv-org/epg](https://github.com/iptv-org/epg) | [`iptv-org/public/channels.xml`](iptv-org/public/channels.xml) | complément : chaînes absentes de xmltvfr (textes dans la langue de la chaîne) |

## Règle d'or pour Kodi

Dans la playlist M3U, le **`tvg-id` doit être exactement l'id XMLTV** de la colonne « tvg-id » :

```
#EXTINF:-1 tvg-id="TF1.fr" tvg-name="TF1 HD" group-title="France",TF1 HD
http://…
```

## Résumé (mesuré le 11/11/2026)

| Statut | Nombre | Signification |
|---|---|---|
| ✅ | 99 | programmes, ≥ 25 % avec résumé et ≥ 50 % avec vignette (les JT/flashs info n'ont souvent pas de résumé) |
| 🟡 | 10 | configurée mais données partielles (peu de programmes, pas de résumé ou pas d'image) |
| ⚠️ | 0 | configurée mais la source n'a rien renvoyé lors du test |
| ❌ | 4 | non configurable (aucune source / chaîne arrêtée) — en commentaire dans `iptv-org/public/channels.xml` |

Colonnes « Résumé » et « Image » = % des programmes qui en ont un. « Progr. » = nombre de programmes / jours couverts.

## Détail par chaîne (triée par id interne)

| Id | Chaîne | Statut | tvg-id | Source | Progr. | Résumé | Image | Remarque |
|---|---|---|---|---|---|---|---|---|
| 1 | 3sat | 🟡 partiel | `3SAT.de` | xmltvfr.fr | 387 / 10 j | 21 % | 96 % |  |
| 2 | AlJazeera English | ✅ | `AlJazeeraEnglish.uk` | xmltvfr.fr | 370 / 10 j | 38 % | 97 % |  |
| 3 | HSE24 HD | ✅ | `HSE.de` | iptv-org · tv.blue.ch | 120 / 6 j | 100 % | 100 % |  |
| 4 | DELUXE Music | ✅ | `DeluxeMusic.de` | iptv-org · tv.blue.ch | 70 / 6 j | 100 % | 100 % |  |
| 5 | RTL+ Germany | ✅ | `RTLPlus.de` | xmltvfr.fr | 230 / 10 j | 100 % | 99 % | supposé = RTLup (ex-RTLplus) |
| 6 | Bayerisches FS Sud | ✅ | `BRFernsehenSud.de` | iptv-org · teleboy.ch | 173 / 6 j | 72 % | 100 % |  |
| 7 | Bibel TV | ✅ | `BibelTV.de` | iptv-org · tv.blue.ch | 259 / 6 j | 99 % | 100 % |  |
| 8 | ARD-Alpha | ✅ | `ARDalpha.de` | iptv-org · tv.blue.ch | 220 / 6 j | 99 % | 100 % |  |
| 10 | CNBC Europe | ✅ | `CNBCEurope.uk` | iptv-org · tv.blue.ch | 210 / 6 j | 100 % | 100 % |  |
| 11 | CNN International Europe | ✅ | `CNNInternational.us` | iptv-org · tv.blue.ch | 165 / 6 j | 100 % | 100 % |  |
| 13 | Das Erste HD | ✅ | `DasErste.de` | xmltvfr.fr | 363 / 10 j | 50 % | 100 % |  |
| 14 | DMAX | ✅ | `DMAX.de` | iptv-org · tv.blue.ch | 135 / 6 j | 100 % | 100 % |  |
| 15 | Tagesschau24 HD | ✅ | `tagesschau24.de` | iptv-org · tv.blue.ch | 185 / 6 j | 99 % | 100 % |  |
| 16 | One | ✅ | `One.de` | iptv-org · tv.blue.ch | 138 / 6 j | 100 % | 100 % |  |
| 18 | EuroNews | ✅ | `Euronews.fr` | xmltvfr.fr | 981 / 10 j | 81 % | 93 % | version française |
| 19 | EuroSport Germany | ✅ | `Eurosport1Germany.de` | iptv-org · tv.blue.ch | 76 / 6 j | 95 % | 100 % |  |
| 20 | TVE International | 🟡 partiel | `TVEInternacional.es` | iptv-org · epgshare01.online | 60 / 4 j | 100 % | 0 % | titre + résumé, pas d'image |
| 22 | France24 English | 🟡 partiel | `France24English.fr` | iptv-org · epgshare01.online | 371 / 4 j | 100 % | 0 % | titre + résumé, pas d'image |
| 23 | France24 France | ✅ | `France24.fr` | xmltvfr.fr | 1017 / 10 j | 33 % | 100 % |  |
| 24 | France 3 | ✅ | `France3.fr` | xmltvfr.fr | 448 / 10 j | 80 % | 100 % | édition nationale |
| 25 | France 4 | ✅ | `France4.fr` | xmltvfr.fr | 815 / 10 j | 81 % | 100 % |  |
| 26 | France 5 | ✅ | `France5.fr` | xmltvfr.fr | 625 / 10 j | 73 % | 100 % |  |
| 27 | France O | ❌ non configurable | — | — | — | — | — | chaîne arrêtée en 2020 |
| 29 | HR | ✅ | `hrfernsehen.de` | iptv-org · tv.blue.ch | 198 / 6 j | 99 % | 100 % |  |
| 30 | Kabel Eins Doku | ✅ | `kabeleinsDoku.de` | iptv-org · tv.blue.ch | 184 / 6 j | 99 % | 100 % |  |
| 31 | Kabel Eins HD | ✅ | `KabelEins.de` | xmltvfr.fr | 241 / 10 j | 100 % | 100 % |  |
| 32 | KI.KA | ✅ | `KIKA.de` | xmltvfr.fr | 428 / 10 j | 100 % | 100 % |  |
| 33 | N24 Doku | ✅ | `N24Doku.de` | iptv-org · tv.blue.ch | 155 / 6 j | 97 % | 100 % | devenue « WELT Doku » |
| 34 | Tele5 | ✅ | `TELE5.de` | iptv-org · tv.blue.ch | 109 / 6 j | 100 % | 100 % |  |
| 35 | TOGGO Plus | ✅ | `TOGGOplus.de` | iptv-org · tv.blue.ch | 315 / 6 j | 100 % | 100 % |  |
| 36 | MDR | ✅ | `MDRFernsehen.de` | iptv-org · tv.blue.ch | 184 / 6 j | 97 % | 100 % | édition Sachsen |
| 37 | Vox UP | ✅ | `Voxup.de` | iptv-org · tv.blue.ch | 137 / 6 j | 100 % | 100 % |  |
| 38 | LCI HD | ✅ | `LCI.fr` | xmltvfr.fr | 131 / 10 j | 41 % | 100 % |  |
| 39 | WELT | ✅ | `WELT.de` | iptv-org · tv.blue.ch | 309 / 6 j | 100 % | 100 % |  |
| 40 | NDR MV | ✅ | `NDRFernsehen.de` | iptv-org · tv.blue.ch | 194 / 6 j | 99 % | 100 % | grille NDR Hamburg (décrochages régionaux différents) |
| 43 | Phoenix | ✅ | `phoenix.de` | iptv-org · tv.blue.ch | 139 / 6 j | 98 % | 100 % |  |
| 46 | Rai Uno | ✅ | `Rai1.it` | iptv-org · tv.blue.ch | 157 / 6 j | 100 % | 100 % |  |
| 47 | Rai Due | ✅ | `Rai2.it` | iptv-org · tv.blue.ch | 173 / 6 j | 99 % | 100 % |  |
| 48 | Rai Tre | ✅ | `Rai3.it` | iptv-org · tv.blue.ch | 183 / 6 j | 100 % | 100 % |  |
| 49 | RadioBremenTV | ✅ | `RadioBremenFernsehen.de` | iptv-org · teleboy.ch | 213 / 6 j | 83 % | 100 % |  |
| 50 | RBB | ✅ | `rbbFernsehen.de` | iptv-org · tv.blue.ch | 178 / 6 j | 99 % | 100 % |  |
| 51 | Record Internacional | ❌ non configurable | — | — | — | — | — | aucune source trouvée |
| 52 | EuroNewsDE | ✅ | `EuronewsGerman.fr` | iptv-org · tv.blue.ch | 485 / 6 j | 100 % | 100 % |  |
| 53 | EuroNewsEN | ✅ | `EuronewsEnglish.fr` | iptv-org · tv.blue.ch | 521 / 6 j | 100 % | 100 % |  |
| 54 | EuroNewsRU | ✅ | `EuronewsRussian.fr` | iptv-org · web.magentatv.de | 43 / 5 j | 100 % | 100 % |  |
| 57 | Sport1 | ✅ | `Sport1.de` | iptv-org · tv.blue.ch | 85 / 6 j | 100 % | 100 % |  |
| 58 | SRFernsehen | ✅ | `SRF1.ch` | xmltvfr.fr | 403 / 10 j | 41 % | 96 % |  |
| 59 | Super RTL | ✅ | `SuperRTL.de` | xmltvfr.fr | 596 / 10 j | 89 % | 100 % |  |
| 64 | TV5MONDE | ✅ | `TV5Monde.fr` | xmltvfr.fr | 463 / 10 j | 69 % | 100 % |  |
| 70 | WDR | ✅ | `WDRFernsehen.de` | iptv-org · teleboy.ch | 186 / 6 j | 77 % | 100 % | édition Köln |
| 73 | ZDFinfokanal | ✅ | `ZDFinfo.de` | iptv-org · tv.blue.ch | 178 / 6 j | 96 % | 100 % |  |
| 74 | ZDFneo | ✅ | `ZDFneo.de` | iptv-org · tv.blue.ch | 175 / 6 j | 100 % | 100 % |  |
| 77 | BBC World News | ✅ | `BBCWorldNews.uk` | xmltvfr.fr | 580 / 10 j | 52 % | 100 % | « BBC News » international |
| 78 | RTL TVI | ✅ | `RTLTVI.be` | xmltvfr.fr | 267 / 10 j | 52 % | 100 % |  |
| 79 | Club RTL | ✅ | `ClubRTL.be` | xmltvfr.fr | 136 / 10 j | 92 % | 100 % |  |
| 80 | RTL 4 | ✅ | `RTL4.nl` | iptv-org · tvgids.nl | 278 / 7 j | 100 % | 99 % | résumés courts |
| 81 | RTL 5 | ✅ | `RTL5.nl` | iptv-org · tvgids.nl | 100 / 7 j | 100 % | 99 % | résumés courts |
| 82 | RTL 7 | ✅ | `RTL7.nl` | iptv-org · tvgids.nl | 131 / 7 j | 100 % | 99 % | résumés courts |
| 83 | Plug RTL | ✅ | `PlugRTL.be` | xmltvfr.fr | 134 / 10 j | 79 % | 100 % |  |
| 85 | 2. RTL | ✅ | `RTL2.de` | xmltvfr.fr | 218 / 10 j | 95 % | 100 % | supposé = RTL Zwei (même guide que « RTL2 HD ») |
| 86 | RTL Letz HD | ❌ non configurable | — | — | — | — | — | aucune source trouvée |
| 97 | TMC | ✅ | `TMC.fr` | xmltvfr.fr | 179 / 10 j | 87 % | 99 % |  |
| 98 | ZDF HD | ✅ | `ZDF.de` | xmltvfr.fr | 320 / 10 j | 71 % | 99 % |  |
| 99 | M6 HD | ✅ | `M6.fr` | xmltvfr.fr | 218 / 10 j | 60 % | 100 % |  |
| 100 | TF1 HD | ✅ | `TF1.fr` | xmltvfr.fr | 253 / 10 j | 75 % | 100 % |  |
| 101 | France 2 HD | ✅ | `France2.fr` | xmltvfr.fr | 369 / 10 j | 60 % | 100 % |  |
| 102 | 1TVRUS Europe | ❌ non configurable | — | — | — | — | — | source testée (tv.blue.ch) : 0 programme |
| 104 | RTP Internacional | 🟡 partiel | `RTPInternacional.pt` | iptv-org · epgshare01.online | 67 / 4 j | 97 % | 0 % | titre + résumé, pas d'image |
| 107 | Bloomberg Tv | ✅ | `BloombergUKEurope.uk` | xmltvfr.fr | 207 / 10 j | 47 % | 100 % |  |
| 134 | La Une HD | ✅ | `LaUne.be` | xmltvfr.fr | 380 / 10 j | 91 % | 99 % |  |
| 135 | la deux | ✅ | `LaDeux.be` | xmltvfr.fr | 220 / 10 j | 93 % | 96 % | devenue « Tipik » |
| 138 | Rai News | ✅ | `RaiNews24.it` | iptv-org · tv.blue.ch | 357 / 6 j | 100 % | 100 % |  |
| 141 | Canal 24 Horas | 🟡 partiel | `Canal24Horas.es` | iptv-org · epgshare01.online | 95 / 4 j | 100 % | 0 % | titre + résumé, pas d'image |
| 142 | RTLNitro | ✅ | `Nitro.de` | iptv-org · tv.blue.ch | 152 / 6 j | 100 % | 100 % |  |
| 143 | Arte (Germany) HD | ✅ | `Arte.de` | xmltvfr.fr | 202 / 10 j | 80 % | 100 % |  |
| 145 | SWR RP HD | ✅ | `SWR.de` | xmltvfr.fr | 316 / 10 j | 100 % | 100 % |  |
| 150 | SAT.1 HD | ✅ | `Sat1.de` | xmltvfr.fr | 230 / 10 j | 100 % | 100 % |  |
| 151 | Prosieben HD | ✅ | `ProSieben.de` | xmltvfr.fr | 358 / 10 j | 70 % | 100 % |  |
| 154 | W9 | ✅ | `W9.fr` | xmltvfr.fr | 197 / 10 j | 80 % | 100 % |  |
| 156 | CStar HD | ✅ | `CStar.fr` | xmltvfr.fr | 276 / 10 j | 60 % | 100 % |  |
| 157 | CNews HD | ✅ | `CNews.fr` | xmltvfr.fr | 557 / 10 j | 60 % | 100 % |  |
| 165 | ARTE France HD | ✅ | `Arte.fr` | xmltvfr.fr | 288 / 10 j | 78 % | 99 % |  |
| 167 | N-tv HD | ✅ | `ntv.de` | iptv-org · tv.blue.ch | 256 / 6 j | 100 % | 100 % |  |
| 168 | RTL2 HD | ✅ | `RTL2.de` | xmltvfr.fr | 218 / 10 j | 95 % | 100 % |  |
| 169 | SIXX HD | ✅ | `sixx.de` | iptv-org · tv.blue.ch | 150 / 6 j | 100 % | 100 % |  |
| 170 | VOX HD | ✅ | `Vox.de` | xmltvfr.fr | 266 / 10 j | 82 % | 100 % |  |
| 171 | RTL HD | ✅ | `RTL.de` | iptv-org · tv.blue.ch | 111 / 6 j | 100 % | 100 % |  |
| 189 | La Trois | ✅ | `LaTrois.be` | xmltvfr.fr | 457 / 10 j | 64 % | 99 % |  |
| 193 | Pro7 Maxx HD | ✅ | `ProSiebenMaxx.de` | iptv-org · tv.blue.ch | 213 / 6 j | 100 % | 100 % |  |
| 194 | USHUAIA TV HD | ✅ | `UshuaiaTV.fr` | xmltvfr.fr | 222 / 10 j | 95 % | 100 % |  |
| 195 | Rai Scuola | ✅ | `RaiScuola.it` | iptv-org · tv.blue.ch | 205 / 6 j | 100 % | 100 % |  |
| 196 | Rai Storia | ✅ | `RaiStoria.it` | iptv-org · tv.blue.ch | 194 / 6 j | 100 % | 100 % |  |
| 197 | Sat.1 Gold | ✅ | `SAT1Gold.de` | iptv-org · tv.blue.ch | 160 / 6 j | 100 % | 100 % |  |
| 198 | Disney Channel Germany | ✅ | `DisneyChannel.de` | iptv-org · tv.blue.ch | 285 / 6 j | 100 % | 100 % |  |
| 199 | Eleven Sport 1 HD | ✅ | `ElevenSports1FR.be` | xmltvfr.fr | 147 / 10 j | 100 % | 71 % | version FR |
| 200 | Eleven Sport 2 HD | ✅ | `ElevenSports2FR.be` | xmltvfr.fr | 172 / 10 j | 99 % | 74 % | version FR |
| 201 | France Info | 🟡 partiel | `FranceInfo.fr` | xmltvfr.fr | 179 / 10 j | 1 % | 100 % |  |
| 204 | SIC | 🟡 partiel | `SICInternacional.pt` | iptv-org · tv.sfr.fr | 35 / 5 j | 0 % | 100 % | SIC Internacional |
| 205 | SIC Noticias | 🟡 partiel | `SICNoticias.pt` | iptv-org · tv.sfr.fr | 35 / 5 j | 0 % | 100 % |  |
| 206 | TVI International | ✅ | `TVIInternacional.pt` | iptv-org · tv.sfr.fr | 86 / 5 j | 85 % | 100 % |  |
| 207 | TVI Ficcao | ✅ | `TVIFiccao.pt` | iptv-org · tv.sfr.fr | 88 / 5 j | 100 % | 100 % | renommée « V+ TVI » |
| 210 | Be1 HD | ✅ | `Be1.be` | xmltvfr.fr | 152 / 10 j | 89 % | 97 % |  |
| 211 | Be1 + 1H | ✅ | `BE1Plus1H.be` | xmltvfr.fr | 150 / 10 j | 99 % | 99 % |  |
| 212 | Be Series | ✅ | `BeSeries.be` | xmltvfr.fr | 164 / 10 j | 92 % | 99 % |  |
| 213 | Be Cine | ✅ | `BeCine.be` | xmltvfr.fr | 122 / 10 j | 93 % | 94 % |  |
| 214 | Voosport 1 | ✅ | `VOOSportWorld1.be` | xmltvfr.fr | 86 / 10 j | 33 % | 78 % | supposé = VOO Sport World 1 |
| 215 | Voosport 2 | ✅ | `VOOSportWorld2.be` | xmltvfr.fr | 63 / 10 j | 67 % | 83 % | supposé = VOO Sport World 2 |
| 216 | Voosport 3 | 🟡 partiel | `VOOSportWorld3.be` | xmltvfr.fr | 9 / 1 j | 100 % | 100 % | supposé = VOO Sport World 3 ; très peu de programmes |
| 217 | Chamber TV HD | 🟡 partiel | `ChamberTV.lu` | iptv-org · tv.post.lu | 8 / 5 j | 0 % | 0 % | très peu de programmes |
| 219 | PlaySports 1 | ✅ | `PlaySports1.be` | iptv-org · telenet.tv | 66 / 6 j | 100 % | 100 % |  |
| 220 | PlaySports 2 (dazn) | ✅ | `PlaySports2.be` | iptv-org · telenet.tv | 21 / 6 j | 100 % | 100 % |  |
| 221 | Luxe TV | ✅ | `LuxeTV.fr` | xmltvfr.fr | 560 / 10 j | 25 % | 68 % |  |
| 222 | CGTN Francais | ✅ | `CGTN.fr` | xmltvfr.fr | 240 / 10 j | 66 % | 51 % |  |

## Modifier la liste

- **Chaîne disponible dans xmltvfr** : ajouter son id dans `xmltvfr/channels.txt` (ids : <https://xmltvfr.fr/channels.php>).
- **Sinon** : chercher la chaîne dans `iptv-org/epg/sites/*/*.channels.xml` (<https://github.com/iptv-org/epg/tree/master/sites>),
  copier la ligne `<channel …>` dans `iptv-org/public/channels.xml` et lui donner un `xmltv_id` unique.
- Puis : `docker compose restart` dans `iptv-org/` (grab immédiat), puis dans `xmltvfr/` (fusion).

## Limites connues

- Les sources sont des sites scrapés : une source peut casser ou bloquer du jour au lendemain (ex. pickx.be renvoie 403).
- Éditions régionales approchées : NDR MV = grille NDR Hamburg, MDR = Sachsen, WDR = Köln (les décrochages régionaux diffèrent).
- Les sources iptv-org fournissent parfois l'image en `<image>` : le script de fusion la recopie en `<icon>`, seule balise lue par Kodi.
