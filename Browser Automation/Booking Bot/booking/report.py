#File includes a class with instance methods responsible to output the hotels we have found from our search

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 

class BookingReport:
    def __init__(self, hotels_element:WebElement):
        self.hotels_element = hotels_element
        self.hotels = self.hotels_element.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')
        #print(len(self.hotels))

    def get_attributes(self):
        collection = []
        for hotel in self.hotels:
            hotelName = hotel.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]').get_attribute('innerHTML').strip()
            hotelName = str(hotelName.replace("&amp;", "&"))

            try:
                hotelScore = hotel.find_element(By.CSS_SELECTOR, 'div[class="b5cd09854e d10a6220b4"]')
            except NoSuchElementException:
                #print("EXCEPTION CAUGHT with")
                #print(hotelName)
                hotelScore = ""
            else:
                hotelScore = hotelScore.get_attribute('innerHTML').strip()

            hotelPrice = hotel.find_element(By.CSS_SELECTOR, 'span[class="fcab3ed991 bd73d13072"]').get_attribute('innerHTML').strip()
            #print(hotelName, hotelScore, hotelPrice)
            collection.append([hotelName, hotelScore, hotelPrice])
        return collection




