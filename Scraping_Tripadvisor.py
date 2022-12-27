import sys
import csv
from selenium import webdriver
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver.maximize_window()

# default path to file to store data
path_to_file = "sofitel_marrakesh.csv"

# default number of scraped pages
#num_page = 300
# if (len(sys.argv) == 4):
#     path_to_file = sys.argv[1]
#     num_page = int(sys.argv[2])
#     url = sys.argv[3]

#url = "https://www.tripadvisor.com/Hotel_Review-g60763-d1218720-Reviews-The_Standard_High_Line-New_York_City_New_York.html"
#url = "https://www.tripadvisor.com/Attraction_Review-g187791-d192285-Reviews-Colosseum-Rome_Lazio.html"
#url="https://www.tripadvisor.com/Hotel_Review-g293734-d302479-Reviews-Movenpick_Hotel_Mansour_Eddahbi_Marrakech-Marrakech_Marrakech_Safi.html"

url="https://www.tripadvisor.fr/Hotel_Review-g293734-d299685-Reviews-Sofitel_Marrakech_Lounge_Spa_Hotel-Marrakech_Marrakech_Safi.html"

# import the webdriver
driver.get(url)

# open the file to save the review
csvFile = open(path_to_file, 'w', encoding="utf-8")
csvWriter = csv.writer(csvFile)


#for i in range(0, num_page):
indexfin=True
i=0
while (indexfin):
    # expand the review
    print('Page:'+str(i))
    i=i+1
    time.sleep(3)
    review_per_page=0
    container = driver.find_elements(By.XPATH, "//div[@data-reviewid]")
    for j in range(len(container)):
        #print(j)
        try:
            rating = container[j].find_element(By.XPATH, ".//span[contains(@class, 'ui_bubble_rating bubble_')]").get_attribute( "class").split("_")[3].replace('0', '')

            title = container[j].find_element(By.XPATH,".//div[contains(@data-test-target, 'review-title')]").text
            review = container[j].find_element(By.XPATH, ".//q[@class='QewHA H4 _a']").text.replace("\n", "  ")
            datestxt = container[j].find_element(By.XPATH, ".//span[@class='teHYY _R Me S4 H3']").text
            x = datestxt.find(":")
            dates = datestxt[x + 1:]
            # print(title)
            csvWriter.writerow([dates, rating, title, review])
        except NoSuchElementException:
            break



        # change the page

    try:
        btnenabled=driver.find_element(By.XPATH,'.//a[@class="ui_button nav next primary "]')
        driver.find_element(By.XPATH, './/a[@class="ui_button nav next primary "]').click()

        # break
    except NoSuchElementException:
        print('Fin')
        indexfin=False
        break







driver.quit()


