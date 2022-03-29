"""Login into https://demoqa.com/login 
(Note: you need to create a user to perform successful flow of login.)
"""
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

USERNAME = "darshak.kakani"
PASSWORD = "Password@123"

if __name__ == "__main__":
    s = Service("./webdrivers/chromedriver")
    driver = webdriver.Chrome(service=s)
    driver.get("https://demoqa.com/login")
    driver.implicitly_wait(5)
    #get locator
    username_input = driver.find_element(By.ID,"userName")
    username_input.send_keys(USERNAME)
    time.sleep(1)
    password_input = driver.find_element(By.ID,"password")
    password_input.send_keys(PASSWORD)
    time.sleep(1)    
    login_btn = driver.find_element(By.ID,"login")
    #submit form
    login_btn.click()
    time.sleep(2)
    driver.quit()