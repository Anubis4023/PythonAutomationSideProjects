from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

#code block to surpress warning messages that come from a bug
options = webdriver.ChromeOptions() 
# to supress the error messages/logs
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#use service to avoid deprecated warnings from selenium
s = Service(r"C:/Users/pacow/Desktop/Selenium Drivers/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=s)
driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
driver.implicitly_wait(3)

try:
    noButton = driver.find_element(By.CLASS_NAME, 'at-cm-no-button')
    noButton.click()
except:
    print("Ad did not pop up. Skipping...")

sum1 = driver.find_element(By.ID, 'sum1')
sum2 = driver.find_element(By.ID, 'sum2')

sum1.send_keys(10)
sum2.send_keys(15)

calc = driver.find_element(By.CSS_SELECTOR, 'button[onclick="return total()"]')
calc.click()


