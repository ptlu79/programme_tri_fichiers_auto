import os
from glob import glob
import shutil
from pprint import pprint


# enlever r devant le chemin si vous n'etes pas sous windows
chemin = r"\Users\grbro\OneDrive\Images"

# ==>  "format" : "dossier de rangement"
extensions = {".svg": "SVG",
              ".jpeg": "JPEG",
              ".jpg": "JPEG",
              ".png": "PNG",
              ".ico": "ICONE"}

# creation des dossiers s'ils n'existent pas bien sur
for value in extensions.values():
    dossier_tri = os.path.join(chemin, value)
    os.makedirs(dossier_tri, exist_ok=True)

#  recupere les chemins de chaque fichier contenu dans chemin
fichiers = glob(os.path.join(chemin, "*"))

# pprint(fichiers) # simple verification

for fichier in fichiers:
    # on recupere le dernier element du splitext soit l'extension de chaque fichier
    extension = os.path.splitext(fichier)[-1]
    # je verifie que l'extension correspond à ma liste de dossier sinon none
    dossier = extensions.get(extension)

# si dossier = none = rien
    if dossier:
        
        chemin_dossier = os.path.join(chemin, dossier)
        # attendre 3 secondes ... ca deplace !!!
        shutil.move(fichier, chemin_dossier)
