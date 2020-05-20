from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

options = Options()
options.add_argument("--headless")
file = open('scraping/results_scrap.txt', 'r')
binary = FirefoxBinary()
browser = webdriver.Firefox(firefox_binary=binary, options=options)
driver = webdriver.Firefox()
for line in file.readlines():
    driver.get("https://reports.exodus-privacy.eu.org/fr/reports/"+ line+"/latest/")
    #elem = driver.find_element_by_name("query")
    #elem.send_keys(line)
    #elem.send_keys(Keys.RETURN)
    if driver.title == "εxodus":
        name = driver.find_element_by_class_name("main-title").text
        print(name)
        #try:
        number_pisteur = driver.find_element_by_xpath('//span[@class="badge badge-pill badge-warning reports"]').text
        print(number_pisteur)
        # pisteur_names = driver.find_element_by_class_name("link black")
        # print(pisteur_names)
        # number_permissions = driver.find_element_by_class_name("badge badge-pill badge-danger reports")
        # print(number_permissions)
        # permissions_names = driver.find_element_by_class_name("text-truncate")
        # print(permissions_names)
        #except Exception:
        print("error")

        



