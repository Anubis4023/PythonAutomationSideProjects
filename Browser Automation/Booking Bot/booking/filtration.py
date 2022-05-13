#This file will include a class with instance methods responsible to filter the search of our results of the booking website
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def apply_star_rating(self, *stars):
        star_filtration = self.driver.find_element(By.CSS_SELECTOR, 'div[data-filters-group="class"]')
        star_filtration_children = star_filtration.find_elements(By.CSS_SELECTOR, '*')
        
        for star in stars:
            #print(f'Looking for {star} stars')
            for child_filter in star_filtration_children:
                if ((str(child_filter.get_attribute('innerHTML')).strip() == '1 star') and star == 1) or (str(child_filter.get_attribute('innerHTML')).strip() == f'{star} stars'):
                    child_filter.click()
                    
    def sort_price_lowest_first (self):
        lowPrice = self.driver.find_element(By.CSS_SELECTOR, 'li[data-id="price"]')
        lowPrice.click()

        
    