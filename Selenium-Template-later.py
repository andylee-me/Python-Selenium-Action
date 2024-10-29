from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller

from pathlib import Path
import pandas as pd
import time
import os
from os.path import exists
import shutil
import csv

# The following 3 lines are for ubuntu only. If windows, please comments then to work well..
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
#                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path


def getDownLoadedFileNameClose():
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
def getDownLoadedFileName():
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get('chrome://downloads')
    #driver.get_screenshot_as_file("page.png")
    return driver.execute_script("return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('div#content  #file-link').text")
 
  
downloadDir = f"{os.getcwd()}//"
preferences = {"download.default_directory": downloadDir,
                "download.prompt_for_download": False,
                "directory_upgrade": True,
                "safebrowsing.enabled": True}
chrome_options = webdriver.ChromeOptions()  

chrome_options.add_experimental_option("prefs", preferences)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument("--window-size=1200,1200")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--no-sandbox")

    
driver = webdriver.Chrome(options = chrome_options)

#driver.get('http://github.com')
#print(driver.title)
#with open('./GitHub_Action_Results.txt', 'w') as f:
#    f.write(f"This was written with a GitHub action {driver.title}")

driver.get('https://www.tpex.org.tw/zh-tw/esb/trading/info/stock-pricing.html')
time.sleep(2)

#read google-sheets
url = "https://raw.githubusercontent.com/andylee-me/Python-Selenium-Action/main/%E7%AB%B6%E5%83%B9%E6%8B%8D%E8%B3%A3.csv"
code = pd.read_csv(url)

print("這是證券代號:",code["證券代號"][0],"\n\n\n\n\n\n")



  #if month...
print("\n\nthisis codeshape",code.shape[0],"\n\n")
for j in range(0,2):
    for i in range(0,code.shape[0]):
        element = driver.find_element(by=By.CLASS_NAME, value="code")
        element.click()
        code_send = list(str(code["證券代號"][i]))
        element.send_keys(code_send)
        time.sleep(0.5)
    
        month = list(code["撥券日期(上市、上櫃日期)"])

        #tiding
        month_pass = ""
        for k in range(0,code.shape[0]):
            month_pass = month_pass+month[k]+"/"
        month = month_pass.split("/")
        month.pop(-1)

        month = list(map(int,month))

        if month[1+i*3] == 1 and j == 1:
            month[1+i*3] += 12
            s = driver.find_element(by=By.CLASS_NAME, value="select-year")
            Select(s).select_by_index(1)
        s = driver.find_element(by=By.CLASS_NAME, value="select-month")
        Select(s).select_by_index(month[1+i*3]-j-1)


        element = driver.find_element(by=By.CLASS_NAME, value="response")
        element.click()
        time.sleep(2)
        
        #driver.get_screenshot_as_file("page.png")
        latestDownloadedFileName = getDownLoadedFileName() 
        time.sleep(2)
        #driver.get_screenshot_as_file("page1.png")
        getDownLoadedFileNameClose()
        DownloadedFilename=''.join(latestDownloadedFileName).encode().decode("utf-8")

        print("\n\nThisis DownloadedFilename:",DownloadedFilename,"\n\n")
        df = DownloadedFilename
        filename = code["撥券日期(上市、上櫃日期)"]+".csv"
        df.to_csv(filename, index=False)
        print(f"{filename} 已成功生成！")
      
        if DownloadedFilename != "OTC.csv":
            # Copy the file to "OTC.csv"
            shutil.copy(DownloadedFilename, "OTC.csv")
            print(f"File '{DownloadedFilename}' copied to 'OTC.csv'.")
            # Delete the original downloaded file
            os.remove(DownloadedFilename)
            print("Download completed...",downloadDir+'OTC.csv')
