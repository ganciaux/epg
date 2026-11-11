"""Construit le guide final pour Kodi.

1. Télécharge le XMLTV complet de xmltvfr.fr et ne garde que les chaînes de channels.txt.
2. Fusionne les guides additionnels (EXTRA_FILES, ex: sortie d'iptv-org) pour les chaînes
   absentes de xmltvfr. En cas de doublon d'id, xmltvfr est prioritaire.
3. Compatibilité Kodi : si un programme n'a pas de <icon> mais a une <image>, on crée le <icon>
   (PVR IPTV Simple ne lit que <icon>).

Pourquoi filtrer : le fichier complet fait ~140 Mo décompressé (780 chaînes) ;
Kodi le parse à chaque rafraîchissement, ce qui est lent (surtout sur Android TV / Raspberry).
"""
import gzip
import os
import shutil
import tempfile
import urllib.request
import xml.etree.ElementTree as ET

SOURCE_URL = os.environ.get("SOURCE_URL", "https://xmltvfr.fr/xmltv/xmltv.xml.gz")
CHANNELS_FILE = os.environ.get("CHANNELS_FILE", "/app/channels.txt")
EXTRA_FILES = [f for f in os.environ.get("EXTRA_FILES", "").split(",") if f.strip()]
OUT_DIR = os.environ.get("OUT_DIR", "/data")


def load_channels(path):
    """Une chaîne par ligne ; tout ce qui suit '#' est un commentaire."""
    with open(path, encoding="utf-8") as f:
        ids = (line.split("#", 1)[0].strip() for line in f)
        return {i for i in ids if i}


def open_xml(path):
    return gzip.open(path) if path.endswith(".gz") else open(path, "rb")


def read_guide(path, keep=None):
    """Lit un XMLTV en flux. keep=None => toutes les chaînes ; sinon seulement ces ids."""
    root_attrs, channels, programmes = {}, {}, []
    # iterparse + clear() : lecture en flux, la mémoire reste faible malgré 140 Mo
    for event, el in ET.iterparse(open_xml(path), events=("start", "end")):
        if event == "start":
            if el.tag == "tv":
                root_attrs = dict(el.attrib)
            continue
        if el.tag == "channel" and (keep is None or el.get("id") in keep):
            channels[el.get("id")] = ET.tostring(el, encoding="unicode")
        elif el.tag == "programme" and (keep is None or el.get("channel") in keep):
            add_icon_from_image(el)
            programmes.append((el.get("channel"), ET.tostring(el, encoding="unicode")))
        if el.tag in ("channel", "programme"):
            el.clear()
    return root_attrs, channels, programmes


def add_icon_from_image(prog):
    if prog.find("icon") is None:
        image = prog.find("image")
        if image is not None and (image.text or "").strip():
            ET.SubElement(prog, "icon", src=image.text.strip())


def download(url, dest):
    print(f"Téléchargement {url}", flush=True)
    req = urllib.request.Request(url, headers={"User-Agent": "epg-filter/1.0"})
    with urllib.request.urlopen(req, timeout=300) as r, open(dest, "wb") as f:
        shutil.copyfileobj(r, f)


def write_guide(tmp, root_attrs, channels, programmes):
    tmp_xml = os.path.join(tmp, "guide.xml")
    tv = ET.tostring(ET.Element("tv", root_attrs), encoding="unicode").replace(" />", ">")
    with open(tmp_xml, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + tv + "\n")
        f.writelines(c + "\n" for c in channels.values())
        f.writelines(p + "\n" for _, p in programmes)
        f.write("</tv>\n")
    with open(tmp_xml, "rb") as fi, gzip.open(tmp_xml + ".gz", "wb") as fo:
        shutil.copyfileobj(fi, fo)
    # remplacement atomique : Kodi ne lit jamais un fichier à moitié écrit
    for name in ("guide.xml", "guide.xml.gz"):
        dst = os.path.join(OUT_DIR, name)
        shutil.copy(os.path.join(tmp, name), dst + ".tmp")
        os.replace(dst + ".tmp", dst)


def main():
    wanted = load_channels(CHANNELS_FILE)
    with tempfile.TemporaryDirectory() as tmp:
        src = os.path.join(tmp, "full.xml.gz")
        download(SOURCE_URL, src)
        root_attrs, channels, programmes = read_guide(src, keep=wanted)

        missing = wanted - channels.keys()
        if missing:
            print(f"ATTENTION ids absents de xmltvfr : {sorted(missing)}", flush=True)
        if not programmes:
            raise SystemExit("Aucun programme trouvé : guide existant conservé")

        for extra in EXTRA_FILES:
            if not os.path.exists(extra):
                print(f"Guide additionnel absent (ignoré) : {extra}", flush=True)
                continue
            _, x_channels, x_programmes = read_guide(extra)
            new_ids = x_channels.keys() - channels.keys()  # xmltvfr prioritaire
            channels.update({i: x_channels[i] for i in new_ids})
            programmes += [p for p in x_programmes if p[0] in new_ids]
            print(f"+ {extra} : {len(new_ids)} chaînes ajoutées", flush=True)

        write_guide(tmp, root_attrs, channels, programmes)
        print(f"OK : {len(channels)} chaînes, {len(programmes)} programmes -> {OUT_DIR}", flush=True)


if __name__ == "__main__":
    main()
