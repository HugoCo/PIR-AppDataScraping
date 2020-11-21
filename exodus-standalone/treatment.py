import os
import csv
import json
import optparse
import sys
import exodus_analyze
from exodus_analyze import AnalysisHelper

location="/home/hugo/Documents/pir/apps/exodus-standalone/apks"

with open('results_data.csv', 'w', newline='') as file:
    for onefile in os.listdir(location):
        if onefile.endswith(".apk"):
            writer = csv.writer(file)
            row = []
            apk_file = "./apks/" + onefile
            print(onefile)
            analysis = AnalysisHelper(apk_file)
            analysis.load_trackers_signatures()
            report = json.dumps(analysis.create_json_report(), indent=2)
            print(report)
            json_report = analysis.create_json_report()
            print(json.dumps(json_report))
            print(json_report['application']['name'])
            row.append(json_report['application']['name']) #Ajoute le nom de l'application
            row.append(len(json_report['application']['permissions'])) #Ajoute le nombre de permissions
            for i in range (len(json_report['application']['permissions'])): #Ajoute le nom des permissions
                print(json_report['application']['permissions'][i])
                row.append(json_report['application']['permissions'][i])
            for i in range (100-len(json_report['application']['permissions'])): #Remplit les cases jusqu'à 30 pour avoir le même nombre sur chaque appli
                row.append("")
            print(len(json_report['trackers']))
            row.append(len(json_report['trackers'])) #Ajoute le nombre de trackers
            for i in range (len(json_report['trackers'])): #Ajoute le nom des trackers
                print(json_report['trackers'][i]['name'])
                row.append(json_report['trackers'][i]['name'])
            writer.writerow(row) #Ajoute la ligne au csv

        
        



