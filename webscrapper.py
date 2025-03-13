# Author: Joel Manakkil
# Date: 14/03/25
# Webscrapper using selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#set path to Chrome Driver
PATH = r"C:\Program Files (x86)\chromedriver-win64\chromedriver.exe"

#initalise webdriver
service = Service(PATH)
driver = webdriver.Chrome(service=service)

#open webpage
driver.get("https://melbournecatholic.org/directory/parishes") #/p1 to /p18

#extract h4 elements with class "mt=0"
names = driver.find_elements(By.CSS_SELECTOR, "h4.mt-0")

#print extracted name
for name in names:
    print(name.text)

# close webpage
driver.quit()