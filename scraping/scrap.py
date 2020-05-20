import play_scraper
import pprint
import sys

key_word = open('keywords.txt', 'r')
fileR = open("results_scrap.txt", "r")
text_already= fileR.read()
file = open('results_scrap.txt','w')
n=0
file.write(text_already)
for line in key_word.readlines():
        ans=""
        to_search=line.strip()
        print("Mot recherché : "+ to_search)
        france_scraped = play_scraper.search(to_search, page=12, hl='fr',gl='fr')
        for x in france_scraped:
                if ans=="next":
                        break
                else:
                        print(x['title'],"|",x['developer'], "|", x['app_id'])
                        ans=input("Ce dev est public ? (y ou n) : ")
                        if ans == 'y' :
                                file.write(x['app_id']+"\n")

#pprint.pprint(france_scraped)
