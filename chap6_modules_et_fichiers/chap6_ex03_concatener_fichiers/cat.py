
def lire_fichier(fichier):
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            contenu = f.read()  # Lit tout le fichier d'un coup
            print(contenu)
    except FileNotFoundError:
        print(f"ERREUR : Le fichier '{fichier}' n'existe pas.")
    except Exception as e:
        print(f"ERREUR : {e}")


def lire_fichier_char_par_char(fichier):
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            while True:
                char = f.read(1)  # Lire un seul caractère
                if not char:  
                    break
                print(char, end="")  # On affiche sans saut de ligne
    except FileNotFoundError:
        print(f" ERREUR : Le fichier '{fichier}' n'existe pas.")
    except Exception as e:
        print(f" ERREUR : {e}")


def lire_fichier_ligne_par_ligne(fichier):
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            for ligne in f:  # Lire chaque ligne une par une
                print(ligne, end="")  
    except FileNotFoundError:
        print(f" ERREUR : Le fichier '{fichier}' n'existe pas.")
    except Exception as e:
        print(f" ERREUR : {e}")