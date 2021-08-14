from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

website = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(website)
time.sleep(10)

def scrape (): 
    headers = ["name", "lightyears from Earth", "planet Mass", "stellar magnitude", "discovery Date"]
    planetData = []
    for i in range(0,447):
        Soup = BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in Soup.find_all("ul", attrs={"class","exoplanet"}):
            li_tags = ul_tag.find_all("li")
            tempList = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    tempList.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        tempList.append(li_tag.contents[0])
                    except:
                        tempList.append(" ")
            planetData.append(tempList)
        button = browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/section[2]/div/section[2]/div/div/article/div/div[2]/div[1]/div[2]/div[1]/div/nav/span[2]/a")
        button.click()
    print(len(planetData))
    with open("planets_of_the_universe.csv", "w")as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planetData)
scrape()
