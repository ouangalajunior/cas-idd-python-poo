
import os

def chercher_remplacer(input, output, str1, str2):
    # Vérifier si le fichier d'entrée existe
    if not os.path.isfile(input):
        print(f"ERREUR : Le fichier d'entrée '{input}' n'existe pas.")
        return
    
    # Vérifier si le fichier de sortie existe déjà
    if os.path.exists(output):
        print(f"ERREUR : Le fichier de sortie '{output}' existe déjà. ")
        return

    try:
        # Lire le contenu du fichier d'entrée
        with open(input, "r", encoding="utf-8") as f_input:
            content= f_input.read()
        
        # Remplacement de toutes les occurrences
        modifed_content = content.replace(str1, str2)

        # Écriture du contenu modifié dans le fichier de sortie
        with open(output, "w", encoding="utf-8") as f_output:
            f_output.write(modifed_content)
        
        print(f"Les occurrences de '{str1}' ont été remplacées par '{str2}' dans '{output}'.")

    except Exception as e:
        print(f"ERREUR : {e}")
