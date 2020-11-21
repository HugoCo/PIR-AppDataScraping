import os 
# défini une liste vide pour stocker les lignes uniques
ls = []
location="/home/hugo/Documents/pir/apps/exodus-standalone/apks"

# ouvrir le fichier en lecture seule
with open('app_id_public.txt', 'r') as file:
    for apk in os.listdir(location):
        ls.append(os.path.splitext(os.path.basename(apk))[0])
    # copier la ligne dans la liste si elle n'y est pas déjà
        for line in file:
            print(os.path.splitext(os.path.basename(apk))[0])
            print(line)
            if line == os.path.splitext(os.path.basename(apk))[0]:
                ls.remove(line)

# réouvrir le fichier mais en mode écriture (ce qui effacera le contenu existant) et écrire les lignes de la liste
with open("app_id_public_new.txt", 'w') as file:
    for line in ls:
        file.write(line)