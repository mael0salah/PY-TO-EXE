# 🚀 Créateur d'Exécutable Python

Ce script permet de créer un exécutable autonome à partir d'un script Python en utilisant PyInstaller. 🐍➡️💼

## ✨ Fonctionnalités

- 📦 Crée un exécutable standalone à partir d'un script Python
- 🛠️ Utilise PyInstaller pour la conversion
- 🚦 Gère les erreurs et fournit des retours d'information

## 📋 Prérequis

- 🐍 Python 3.x
- 🔧 PyInstaller (installable via `pip install pyinstaller`)

## 🚀 Utilisation

1. Assurez-vous que PyInstaller est installé :
```
pip install pyinstaller
```

3. 🎉 L'exécutable sera créé dans le dossier `dist` si l'opération réussit.
```
python create_executable.py <chemin-vers-votre-script.py>
```

5. 💪 L'exécutable sera créé dans le dossier `dist` si l'opération réussit.
```
dist
```

## Code source

```
import os
import subprocess
import sys

def create_executable(script_path):
    if not os.path.isfile(script_path):
        print(f"Le fichier {script_path} n'existe pas.")
        return

    command = [
        sys.executable, '-m', 'PyInstaller',
        '--onefile',
        '--windowed',
        script_path
    ]

    try:
        result = subprocess.run(command, capture_output=True, text=True)

        print(result.stdout)
        if result.stderr:
            print(result.stderr)

        dist_path = os.path.join('dist', os.path.splitext(os.path.basename(script_path))[0] + '.exe')
        if os.path.isfile(dist_path):
            print(f"L'exécutable a été créé avec succès : {dist_path}")
        else:
            print("Une erreur s'est produite lors de la création de l'exécutable.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_executable.py <path-to-script.py>")
    else:
        create_executable(sys.argv[1])
```


## ⚙️ Fonctionnement

Le script effectue les actions suivantes :

1. Vérifie l'existence du fichier script fourni
2. Utilise PyInstaller pour créer un exécutable autonome
3. Affiche la sortie de PyInstaller
4. Vérifie si l'exécutable a été créé avec succès
5. Gère les erreurs potentielles et les affiche

## 💬 Remarques

- L'option `--windowed` est utilisée, ce qui signifie que l'exécutable ne montrera pas de console lors de son exécution
- L'exécutable créé sera autonome et contiendra toutes les dépendances nécessaires

## ⚠️ Avertissement

Assurez-vous d'avoir les droits nécessaires pour exécuter des scripts et créer des fichiers dans le répertoire de travail.
