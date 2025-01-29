from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webdriver import BaseWebDriver as Base
from selenium.webdriver.chrome.options import Options


import time

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
"download.default_directory": True, #Change default directory for downloads
"download.prompt_for_download": False, #To auto download the file
"download.directory_upgrade": True,
"plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
})
browser = webdriver.Chrome(options=options)

browser.get("https://www.uscis.gov/administrative-appeals/aao-decisions/aao-non-precedent-decisions")
def find_wrapper():
    sel = browser.find_elements(By.CLASS_NAME,"select-wrapper")
    return sel

def find_next_button():
    try:
        next_button = browser.find_element(By.LINK_TEXT,"Next")
        next_button.click()
        time.sleep(3)
    except:
        print("it is the last page")
        pass

def find_month(month,year,file_qty):
    months  = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    years = [2024,2023,2022,2021,2020,2019,2018,2017]
    files = [10,50,100]

    for i in months:
        if i == month:
            n = months.index(month)
    
    month_sel = find_wrapper()[1]
    month_sel.click() #1 is a select-wrapper for  month selection #2 is a select-wrapper for the year selection
    time.sleep(1)
    i=0
    for i in range(n+1):
        month_sel.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.3)
    month_sel.send_keys(Keys.ENTER)
    time.sleep(2)

    year_sel = find_wrapper()[2]
    for i in years:
        if i == year:
            n = years.index(year)
    year_sel.click()
    time.sleep(1)
    i=0
    for i in range(n+1):
        year_sel.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.1)
    year_sel.send_keys(Keys.ENTER)
    time.sleep(2)

    files_sel = find_wrapper()[3]
    for i in files:
        if i == file_qty:
            n = files.index(file_qty)
    files_sel.click()
    time.sleep(1)
    i = 0
    for i in range(n+1):
        files_sel.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.1)
    files_sel.send_keys(Keys.ENTER)
    time.sleep(2)


find_month("June",2022,50)

for i in range(10):
    find_next_button()

time.sleep(5)

for web in range (len(element)):
    browser.get("https://www.uscis.gov/administrative-appeals/aao-decisions/aao-non-precedent-decisions")  
    element = browser.find_elements(By.PARTIAL_LINK_TEXT, "PDF")
    elem = element[web].click()
    time.sleep(5)
