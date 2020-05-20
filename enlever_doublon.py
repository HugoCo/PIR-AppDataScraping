# défini une liste vide pour stocker les lignes uniques
ls = []

# ouvrir le fichier en lecture seule
with open('results_scrap.txt', 'r') as file:
    # lire le fichier ligne par ligne
    for line in file:
        # copier la ligne dans la liste si elle n'y est pas déjà
        if line not in ls:
            ls.append(line)

# réouvrir le fichier mais en mode écriture (ce qui effacera le contenu existant) et écrire les lignes de la liste
with open("results_scrap_wo_double.txt", 'w') as file:
    for line in ls:
        file.write(line)