from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class BookingFilter:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def reapply_filters(self): #Reset the filters after going back to the first page
        self.sort_cheapest(option=2)
        self.choose_location(option=2)
        self.filter_brand(option=2)
        self.clear_dates()

    def clear_dates(self):
        buttonWorks = False
        while not buttonWorks:
            try:
                clear = self.driver.find_element(By.CSS_SELECTOR, 'button[class="c-delete-dates delete-dates-JS"]')
                clear.click()
                buttonWorks = True
            except:
                buttonWorks = False
        
    
    def sort_cheapest(self, option=1): #Option one is for the start of the script, option two is for when hotels are being selected
        sort = self.driver.find_element(By.ID, 'search-order')
        sort.click()

        if (option == 2): #sort list opened, click on default sort, open sort list again
            sort_default = self.driver.find_element(By.CSS_SELECTOR, 'option[class="hidden md:block"]')
            sort_default.click()
            sort.click()

        sort_cheapest = self.driver.find_element(By.CSS_SELECTOR, 'option[value="info.hotelLocalLowPrice"]') #sort by lowest price
        sort_cheapest.click()

        sort.click()
        time.sleep(1) #Let page load after filter

    def filter_brand(self, option=1):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

        brands = self.driver.find_element(By.CSS_SELECTOR, 'div[data-dimension="hotel_brand"]')
        brands = brands.find_element(By.CSS_SELECTOR, 'span[class="accordion-toggle mod--icon-right"]')

        try:
            loading = self.driver.find_element(By.CSS_SELECTOR, 'div[class="c-loading c-loading-JS bhg-loading mod--loading-active common-transition mod--fullscreen"]')
            while loading.is_displayed():
                time.sleep(1)
        except:
            pass

        brands.click()

        barcelo = self.driver.find_element(By.CSS_SELECTOR, 'input[name="Barceló"]')

        if (option == 2): #uncheck the barcelo box and then check it again to apply the filter
            barcelo.click()

        barcelo.click()
        time.sleep(1) #Let page load after filter

    def choose_location(self, option=1):
        more_button = self.driver.find_element(By.CSS_SELECTOR, 'div[class="sidebar__facets-list"]')
        more_button = more_button.find_element(By.CSS_SELECTOR, 'div[class="facets-list__toggle-btn"]')
        more_button.click()
        
        location = self.driver.find_element(By.CSS_SELECTOR, 'input[name="Quintana Roo"]')

        if (option == 2): #uncheck the cancun box and then check it again to apply the filter
            location.click()

        location.click()

    def accept_cookies(self):
        accept = self.driver.find_element(By.ID, 'didomi-notice-agree-button')
        accept.click()



