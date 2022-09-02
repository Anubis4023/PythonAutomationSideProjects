from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import os
import time

class Checkbook(webdriver.Chrome):
    def __init__(self, teardown, driver_path=r";C:\Users\pacow\Onedrive\Desktop\Selenium Drivers"):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        os.environ['PATH'] += r";C:\Users\pacow\OneDrive\Desktop\Selenium Drivers"
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Checkbook, self).__init__(options=options)
        self.implicitly_wait(10) #Find element methods will wait x seconds
        self.maximize_window()

    def land_banks(self):
        self.get("https://www.chase.com/")
        

        #Fill out username and password information
        WebDriverWait(self, 10).until(EC.frame_to_be_available_and_switch_to_it((By.NAME,"logonbox")))
        self.find_element(By.ID, 'signin-button').click()
        time.sleep(3)

        username = self.find_element(By.ID, 'userId-text-input-field')
        password = self.find_element(By.ID, 'password-text-input-field')

        WebDriverWait(self, 20).until(EC.element_to_be_clickable(username)).click() #send_keys(os.environ.get("Chase Username"))
        username.send_keys(os.environ.get("Chase Username"))
        time.sleep(3)
        password.click() #send_keys(os.environ.get("Chase Password"))
        password.send_keys(os.environ.get("Chase Password"))
        #Click on login
        time.sleep(3)
        self.find_element(By.ID, 'signin-button').click()



        #WebDriverWait(self, 5).until(EC.element_to_be_clickable(username))
        
        

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.teardown:
            #time.sleep(3)
            self.quit()   