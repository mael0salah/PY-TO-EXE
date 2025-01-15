# Let's write the README content to a markdown (.md) file.

readme_content = """
# README - Script de création d'exécutable Python

## Description

Ce script permet de convertir un fichier Python (.py) en un exécutable (.exe) autonome. Il utilise **PyInstaller**, un outil permettant de créer des exécutables à partir de scripts Python. Ce script crée un fichier exécutable qui pourra être exécuté sur des machines Windows sans nécessiter d'installer Python.

## Fonctionnalités

- Vérifie que le fichier source existe.
- Utilise PyInstaller pour créer un exécutable.
- Crée un fichier exécutable dans le dossier `dist`.
- Gère les erreurs et affiche les messages de sortie.

## Prérequis

1. **Python** (version 3.x) doit être installé sur votre machine.
2. **PyInstaller** doit être installé. Si ce n'est pas le cas, vous pouvez l'installer via pip :

```bash
pip install pyinstaller
