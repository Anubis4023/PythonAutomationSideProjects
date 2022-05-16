from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

import time

class BookingReport:
    def __init__(self, driver:WebDriver, hotels_element:WebElement):
        self.driver = driver
        self.hotels_element = hotels_element
        self.hotels = self.hotels_element.find_elements(By.CSS_SELECTOR, 'div[class="result__list-item"]')

    def search(self): #self.hotels has a list of the hotels, go to each hotel and find the price for each person
                      #in the cheapest room. Later update to also find a Volaris plane ticket 
        self.findPrice(self.hotels[0])

        for hotel in self.hotels: #for each hotel, click on booking, get redirected, get price, close tab, 
                                  #go back to first tab, apply filters again (make it one function), 
                                  #and continue process for every hotel using findPrice on each one
            pass

    def findPrice(self, hotel:WebElement): #working with each invidiual hotel passed into hotel in the main screen
        #Press button to get redirected to hotel booking
        hotelBooking = hotel.find_element(By.CSS_SELECTOR, 'button[class="mod--cta-fullbg mod--cta-full-width mod--cta-color-red booking-button-JS"]')
        
        try:
            loading = self.driver.find_element(By.CSS_SELECTOR, 'div[class="c-loading c-loading-JS bhg-loading mod--loading-active common-transition mod--fullscreen"]')
            while loading.is_displayed():
                time.sleep(1)
                print("Waited one second for loading screen")
        except:
            print("Loading screen done! Exception caught and handled")

        hotelBooking.click()

        #Press the 'Booking' button to begin booking for the hotel
        booking_button = self.driver.find_element(By.ID, 'hotelinfo_cta_booking')
        booking_button.click()

        #Select booking dates
        time.sleep(3) #Let calendar load in
        test = self.driver.find_element(By.ID, 'month-1-1')
        dates = test.find_elements(By.CSS_SELECTOR, 
        'td[class="datepicker__month-day datepicker__month-day--visibleMonth datepicker__month-day--valid mod--loaded"], td[class="datepicker__month-day datepicker__month-day--visibleMonth datepicker__month-day--valid datepicker__month-day--today datepicker__month-day--checkin-only mod--loaded"]'
        )
        #print(len(dates))
        #dates +=  test.find_elements(By.CSS_SELECTOR, '')
        #print(len(dates))
        
        #dates.sort(key=dates.num)
        time.sleep(5) #Let the calendar load in all elements
        prices = []
        numOfDays = 3
        for day in dates:
            prices.append(int(day.find_element(By.CSS_SELECTOR, #Get the element for each day
            'span[class="price-day-calendar mod--green-text"], span[class="price-day-calendar mod--yellow-text"], span[class="price-day-calendar mod--red-text"]'
            ).find_element(By.CSS_SELECTOR, #Get the price for that day
            'span[class="c-price__value c-price__value-JS"]'
            ).get_attribute('innerHTML')))

        print(prices)
        index = self.findCheapestDays(prices)
        print(index)

        print("Cheapest Days are:")
        dates[index[0]].click() #start day
        dates[index[1]].click() #end day


    def findCheapestDays(self, prices): #Find the cheapest three days and return the start day and end day index
        lowestPrice = prices[0] + prices[1] + prices[2]
        print("Lowest price: ", lowestPrice)
        lowestDays = [0, 2]
        for i in range(len(prices)-2):
            if ((prices[i] + prices[i+1] + prices[i+2]) < lowestPrice):
                lowestPrice = prices[i] + prices[i+1] + prices[i+2]
                print("Lowest price: ", lowestPrice)
                lowestDays[0] = i
                lowestDays[1] = i+2
        return lowestDays

