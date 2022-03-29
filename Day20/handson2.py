"""Find all possible locators from https://demoqa.com/automation-practice-form
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def run_browser():
    """This function automat browser functionality
    """
    driver = webdriver.Chrome(executable_path="./webdrivers/chromedriver")
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get('https://demoqa.com/automation-practice-form')
    #firstname
    fname = driver.find_element_by_id('firstName')
    fname.send_keys("Darshak")
    
    #lastname
    lname = driver.find_element_by_id('lastName')
    lname.send_keys("kakani")
    
    #Email
    email_input = driver.find_element_by_xpath("//input[@id='userEmail']")
    email_input.send_keys("darshak@gmail.com")
    
    #Gender
    male_radio = driver.find_element(By.XPATH,"//input[@value='Male']")
    driver.execute_script("arguments[0].click();",male_radio)
    
    #mobile no
    mobile_input = driver.find_element(By.ID, "userNumber")
    mobile_input.send_keys('8823658795')
    
    #DateOfBirth
    date_of_birth_input = driver.find_element(By.ID, "dateOfBirthInput")
    date_of_birth_input.click()
    date_of_birth_input.send_keys(Keys.CONTROL, "a")
    date_of_birth_input.send_keys("16 Sep 2000",Keys.ENTER)
    
    
    #Subject
    subjects_input = driver.find_element(By.ID, "subjectsInput")
    subjects_input.send_keys("English")
    subjects_input.send_keys(Keys.ENTER)
    
    #Checkbox
    sports_checkbox = driver.find_element(By.XPATH,"//input[@value='1']")
    reading_checkbox = driver.find_element(By.XPATH,"//input[@value='2']")
    driver.execute_script("arguments[0].click();arguments[1].click();",sports_checkbox,reading_checkbox)

    # scroll down
    # driver.execute_script("window.scrollTo(0, 800)")
    
    #File input
    upload_picture = driver.find_element(By.ID, "uploadPicture")
    upload_picture.send_keys(r"C:\Users\darshak.kakani\projects\Day18\images\1.jpg")
    
    #Address
    address_input = driver.find_element(By.ID, "currentAddress")
    address_input.send_keys("Surat")
    
    # Handling State Selection
    state_drop_down_menu = driver.find_element(By.ID, "react-select-3-input")
    state_drop_down_menu.send_keys("NCR", Keys.ENTER)

    # Handling City Selection
    city_drop_down_menu = driver.find_element(By.ID, "react-select-4-input")
    city_drop_down_menu.send_keys("Delhi", Keys.ENTER)
    
    #Submit button
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    
    time.sleep(3)
    driver.quit()

if __name__ == "__main__":
    run_browser()