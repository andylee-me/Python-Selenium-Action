from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller

import time
import os
from os.path import exists
import shutil

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

driver.get('https://www.twse.com.tw/zh/announcement/public.html')
time.sleep(2)
element = driver.find_element(by=By.CLASS_NAME, value="csv")
element.click()
time.sleep(2)

#driver.get_screenshot_as_file("page.png")
latestDownloadedFileName = getDownLoadedFileName() 
time.sleep(2)
#driver.get_screenshot_as_file("page1.png")
getDownLoadedFileNameClose()
DownloadedFilename=''.join(latestDownloadedFileName).encode().decode("utf-8")
if DownloadedFilename != "auction.csv":
    # Copy the file to "auction.csv"
    shutil.copy(DownloadedFilename, "auction.csv")
    print(f"File '{DownloadedFilename}' copied to 'auction.csv'.")
    # Delete the original downloaded file
    os.remove(DownloadedFilename)

print("Download completed...",downloadDir+'auction.csv')

