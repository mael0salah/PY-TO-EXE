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
