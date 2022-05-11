from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverwait
from selenium.webdriver.support import expected_conditions as EC

driver_path = r"C:/Users/pacow/Desktop/Selenium Drivers/chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")
driver.implicitly_wait(3)
downloadButton = driver.find_element(By.ID,'downloadButton')
downloadButton.click()

progress_element = #

WebDriverwait(driver, 30).until(
    EC.text_to_be_present_in_element(
        #Element to check

        #Text element should be
    )
)