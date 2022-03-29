"""Read the table content from here and print them in consol.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    s = Service("./webdrivers/chromedriver")
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.w3schools.com/html/html_tables.asp")
    
    rows = driver.find_elements(By.XPATH, "//*[@id='customers']/tbody/tr")
    cols = driver.find_elements(By.XPATH, "//*[@id='customers']/tbody/tr/th")
    
    for header in cols:
        print(header.text+"\t\t\t",end="")
    print()    
    for i in range(2,len(rows) + 1): #Loop to iterate rows   
        Xpath = "//*[@id='customers']/tbody/tr["+str(i)+"]/td"
        row = driver.find_elements(By.XPATH,Xpath)
        for j in row:#get table row content
            print(j.text+"\t",end="")
        print()    
    driver.quit()