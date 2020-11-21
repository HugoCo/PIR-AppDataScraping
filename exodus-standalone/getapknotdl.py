import os 
# défini une liste vide pour stocker les lignes uniques
ls = []
location="/home/hugo/Documents/pir/apps/exodus-standalone/test"

# ouvrir le fichier en lecture seule
with open('app_id_public.txt', 'r') as file:
    for apk in os.listdir(location):
        print(os.path.splitext(os.path.basename(apk))[0])
