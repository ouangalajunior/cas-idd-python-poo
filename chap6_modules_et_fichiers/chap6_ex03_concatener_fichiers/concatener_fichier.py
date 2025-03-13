

def concatener_fichiers(*fichiers):
   
    fichiers_source = fichiers[:-1]  # Tous sauf le dernier
    fichier_destination = fichiers[-1]  # Dernier fichier


    # Concaténation des fichiers sources dans le fichier destination
    try:
        with open(fichier_destination, "w", encoding="utf-8") as dest:
            for fichier in fichiers_source:
                with open(fichier, "r", encoding="utf-8") as src:
                    dest.write(src.read() + "\n")  
        print(f" Contenu des fichiers concaténé dans '{fichier_destination}'")
    except Exception as e:
        print(f" ERREUR : {e}")

