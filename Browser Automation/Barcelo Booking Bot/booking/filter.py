from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class BookingFilter:
    def __init__(self, driver:WebDriver):
        self.driver = driver
    
    def sort_cheapest(self):
        sort = self.driver.find_element(By.ID, 'search-order')
        sort.click()

        sort_cheapest = self.driver.find_element(By.CSS_SELECTOR, 'option[value="info.hotelLocalLowPrice"]')
        sort_cheapest.click()

        sort.click()
        time.sleep(1) #Let page load after filter

    def filter_brand(self):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        #time.sleep(10)

        brands = self.driver.find_element(By.CSS_SELECTOR, 'div[data-dimension="hotel_brand"]')
        brands = brands.find_element(By.CSS_SELECTOR, 'span[class="accordion-toggle mod--icon-right"]')

        try:
            loading = self.driver.find_element(By.CSS_SELECTOR, 'div[class="c-loading c-loading-JS bhg-loading mod--loading-active common-transition mod--fullscreen"]')
            while loading.is_displayed():
                time.sleep(1)
                #print("Waited one second for loading screen")
        except:
            #print("Loading screen done!")
            pass

        brands.click()

        barcelo = self.driver.find_element(By.CSS_SELECTOR, 'input[name="Barceló"]')
        barcelo.click()
        time.sleep(1) #Let page load after filter

    def choose_location(self):
        more_button = self.driver.find_element(By.CSS_SELECTOR, 'div[class="sidebar__facets-list"]')
        more_button = more_button.find_element(By.CSS_SELECTOR, 'div[class="facets-list__toggle-btn"]')
        more_button.click()
        
        location = self.driver.find_element(By.CSS_SELECTOR, 'input[name="Quintana Roo"]')
        location.click()

    def accept_cookies(self):
        accept = self.driver.find_element(By.ID, 'didomi-notice-agree-button')
        accept.click()



