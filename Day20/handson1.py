"""Write a program that 
Open Chrome & Firefox browsers  one after the other and perform all the given actions
Resize the window
maximize the window
Hit the URL: http://www.google.com
Print the title of the tab
Open a new tab
Hit the URL: https://stackoverflow.com
Print the title of the tab
Close the first window
Close the session
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def run_browser():
    """This function automat browser functionality
    """
    driver = webdriver.Chrome(executable_path="./webdrivers/chromedriver")
    driver.implicitly_wait(5)
    driver.set_window_size(1000,500)

    driver.maximize_window()

    driver.get('http://www.google.com/')
    print(driver.title)
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://stackoverflow.com')
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    time.sleep(3)
    driver.quit()

if __name__ == "__main__":
    run_browser()