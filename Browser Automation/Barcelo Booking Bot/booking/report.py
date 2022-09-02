from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from setuptools import find_packages
import re

from booking.filter import BookingFilter
from booking.volaris import Volaris

import time

class BookingReport:
    def __init__(self, driver:WebDriver, hotels_element:WebElement, adults, rooms):
        self.driver = driver
        self.hotels = driver.find_element(By.CSS_SELECTOR, 'div[class="result__list result__list-JS"]').find_elements(By.CSS_SELECTOR, 'div[class="result__list-item"]')
        self.party = adults
        self.rooms = rooms

    def search(self): #self.hotels has a list of the hotels, go to each hotel and find the price for each person
        
        dates = []
        for hotel in range(len(self.hotels)): #Go to each hotel and retreive their name and price and plane ticket price
            listHotels = self.driver.find_element(By.CSS_SELECTOR, 'div[class="result__list result__list-JS"]').find_elements(By.CSS_SELECTOR, 'div[class="result__list-item"]')
            name = listHotels[hotel]
            print(name.find_element(By.CSS_SELECTOR, 'span[class="c-cta"]').get_attribute('innerHTML'))
            info = self.findPrice(hotel)
            print(info[2], "\n")
            self.refilter()

            planeTickets = Volaris(self.driver)
            planeTickets.land_second_page()
            #time.sleep(10)
            planeTickets.find_tickets(info[0], info[1])
            planeTickets.close()
    
    def refilter(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.back()
        filter = BookingFilter(self.driver)
        filter.reapply_filters()


    def findPrice(self, hotel): #working with each invidiual hotel passed into hotel in the main screen
        listHotels = self.driver.find_element(By.CSS_SELECTOR, 'div[class="result__list result__list-JS"]').find_elements(By.CSS_SELECTOR, 'div[class="result__list-item"]')
        hotel = listHotels[hotel]
        info = self.selectCheapestDays(hotel)
        self.selectOccupancy()
        self.signIn(False)
        self.selectRooms()
        info.append(self.pullPrice())
        return info

    def pullPrice(self):
        totalTextDraft = self.driver.find_element(By.CSS_SELECTOR, 'div[class="price-summary_price"]').find_element(By.CSS_SELECTOR, 'span').get_attribute('innerHTML')
        totalText = totalTextDraft[1:] 
        totalText = totalText.replace(",", "")
        total = float(totalText)

        Prices = [] #List of prices in the format: Total price, individual total price, individual price per night
        Prices.append(total)
        Prices.append(total/self.party)
        Prices.append(total/self.party/self.rooms)
        return Prices

    def selectRooms(self):
        numRooms = self.rooms
        for i in range(numRooms):
            #Get the cheapest room
            #rooms_element = self.driver.find_element(By.CSS_SELECTOR, 'div[class="thumb-cards_products"]') #This part is not necessary to finding the cheapest room, but is necessary if I want the option to pick cheapest vs more expensive options
                                                                        #rooms_element is the overall element that holds the list of rooms
            buttonLoaded = False
            while not buttonLoaded:
                try:
                    cheapest_room = self.driver.find_element(By.ID, 'auto-parent-card-0') #instead of rooms_element.find
                    buttonLoaded = True
                except:
                    buttonLoaded = False
            
            #book_button is the button for picking the cheapest room
            buttonLoaded = False
            while not buttonLoaded:
                try: #First button click fails, but second one works
                    book_button = cheapest_room.find_element(By.CSS_SELECTOR, 'button[class="btn button_btn button_primary button_sm"]')
                    book_button.click()
                    buttonLoaded = True
                except:
                    buttonLoaded = False

            #Click on the next room button or don't if it doesn't send us to the second page of additions
            time.sleep(3)
            buttonLoaded = False
            while not buttonLoaded:
                try:
                    continue_button = self.driver.find_element(By.CSS_SELECTOR, 'button[class="btn button_btn button_primary button_md button_block"]')
                    continue_button.click()

                    if i != (numRooms-1):
                        self.signIn(False)

                    buttonLoaded = True
                except ElementNotInteractableException:
                    print("Element not interactable")
                    buttonLoaded = True
                except NoSuchElementException:
                    print("Continue/Next room button does not exist")
                    buttonLoaded = True
                except Exception as e:
                    #print("other exception caught")
                    #print(e)
                    buttonLoaded = False
            
        

    def signIn(self, account):
        while len(self.driver.window_handles) == 1:
            time.sleep(1)

        self.driver.switch_to.window(self.driver.window_handles[1])
        if account: #sign in to account
            pass
        else: #continue as guest
            close_button = self.driver.find_element(By.CSS_SELECTOR, 'button[class="tingle-modal__close tingle-modal__close-JS"]')
            time.sleep(2)
            close_button.click()


    def selectOccupancy(self):
        adults = self.party
        rooms = self.rooms

        #Press button to open list to select number of adults and rooms
        adultsList = self.driver.find_element(By.ID, 'rooms-fb')
        adultsList.click()

        #Split the number of adults equally to the rooms
        roomSize = [int(adults/rooms)] * rooms
        numAdultsLeft = adults % rooms
            
        if (numAdultsLeft != 0): #TODO: #7 Too many people and not enough rooms will cause an error. Notify user that more rooms will be allocated
            #("Number of adults did not divide evenly. Adults left: ", numAdultsLeft)
            for i in range(numAdultsLeft):
                roomSize[i] += 1

        for i in range(rooms): #elements may need to be adjusted when a new room is added
            if i != 0: #if it's not the first room, add another room
                addRoom = self.driver.find_element(By.CSS_SELECTOR, 'div[class="c-cta mod--cta-md mt-4 md:mt-0 mb-5 add-JS"]')
                addRoom.click()
            
            #Add the number of adults for each room
            #Bring down the number of adults to one
            numAdults_elements = self.driver.find_elements(By.CSS_SELECTOR, 'input[class="input-adult input-JS input-adult-JS tooltip-JS tooltip-full-JS"]')
            subAdults_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'div[class="c-incrementers__btn dec-button-JS"]')
            addAdults_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'div[class="c-incrementers__btn inc-button-JS"]')

            for h in range(len(numAdults_elements)):
                if numAdults_elements[h].is_displayed():
                    numAdults_element = numAdults_elements[h]
                    break
                else:
                    numAdults_element = numAdults_elements[-1] #should never get here. arriving here means error in adding number of adults

            numAdults = int(numAdults_element.get_attribute('value'))
            while (numAdults != 1):
                for h in range(len(subAdults_buttons)):
                    if (subAdults_buttons[h].is_displayed()):
                        subAdults = subAdults_buttons[h]
                        break
                    else:
                        subAdults = subAdults_buttons[-1] #Same thing, error if this is reached because none of the buttons we are trying to click are visible
                subAdults.click()
                numAdults = int(numAdults_element.get_attribute('value'))
            #Bring the number of adults up the required amount
            while (numAdults != roomSize[i]):
                for h in range(len(addAdults_buttons)):
                    if (addAdults_buttons[h].is_displayed()):
                        addAdults = addAdults_buttons[h]
                        break
                    else:
                        addAdults = addAdults_buttons[-1]
                addAdults.click()
                numAdults = int(numAdults_element.get_attribute('value'))

        accept_button = self.driver.find_element(By.CSS_SELECTOR, 'div[class="mod--cta-full-width mod--cta-outline mod--cta-outline-with-bg mod--cta-color-grey-90 text-base mt-4 apply-JS"]')
        accept_button.click()

        search_button = self.driver.find_element(By.ID, 'fastbooking_cta_booking_hotel')
        search_button.click()


    def selectCheapestDays(self, hotel:WebElement):
        #Press button to get redirected to hotel booking
        #print("test")
        test = True
        while test:
            try:
                hotelBooking = hotel.find_element(By.CSS_SELECTOR, 'button[class="mod--cta-fullbg mod--cta-full-width mod--cta-color-red booking-button-JS"]')
                test = False
            except:
                print("Trying to click on the 'Booking' button of the hotel")
                test = True
        
        #This second while, try/except block sometimes gets stuck
        buttonWorks = False
        while not buttonWorks:
            try:
                hotelBooking.click()
                buttonWorks = True
            except Exception as e:
                #print(e)
                buttonWorks = False

        #print("got here")
        #Press the 'Booking' button to begin booking for the hotel
        booking_button = self.driver.find_element(By.ID, 'hotelinfo_cta_booking')
        booking_button.click()

        #Select booking dates
        time.sleep(3) #Let calendar load in
        test = self.driver.find_element(By.ID, 'month-2-1')
        dates = test.find_elements(By.CSS_SELECTOR, 
        'td[class="datepicker__month-day datepicker__month-day--visibleMonth datepicker__month-day--valid mod--loaded"], td[class="datepicker__month-day datepicker__month-day--visibleMonth datepicker__month-day--valid datepicker__month-day--today datepicker__month-day--checkin-only mod--loaded"]'
        )

        prices = []
        numOfDays = 3 

        for day in dates:
            staleElement = True
            while (staleElement):
                try:
                    dates = test.find_elements(By.CSS_SELECTOR, 
                    'td[class="datepicker__month-day datepicker__month-day--visibleMonth datepicker__month-day--valid mod--loaded"], td[class="datepicker__month-day datepicker__month-day--visibleMonth datepicker__month-day--valid datepicker__month-day--today datepicker__month-day--checkin-only mod--loaded"]'
                    )
                    prices.append(int(day.find_element(By.CSS_SELECTOR, #Get the element for each day
                        'span[class="price-day-calendar mod--green-text"], span[class="price-day-calendar mod--yellow-text"], span[class="price-day-calendar mod--red-text"]'
                        ).find_element(By.CSS_SELECTOR, #Get the price for that day
                        'span[class="c-price__value c-price__value-JS"]'
                        ).get_attribute('innerHTML')))
                    staleElement = False
                except StaleElementReferenceException:
                    print("Stale element for the calendar. Trying again to see if the calendar prices have loaded")
                    staleElement = True

        cheapest = self.findCheapestDays(prices)

        dayStart = dates[cheapest[0]].get_attribute('innerHTML')
        dayStart = dayStart[-2:]
        dayStart = re.sub('\D', '', dayStart)
        
        dayEnd = dates[cheapest[1]].get_attribute('innerHTML')
        dayEnd = dayEnd[-2:]
        dayEnd = re.sub('\D', '', dayEnd)

        print("Picking days: ", dayStart, " and ", dayEnd)
        dates[cheapest[0]].click() #start day
        dates[cheapest[1]].click() #end day

        return [dayStart, dayEnd]


    def findCheapestDays(self, prices): #Find the cheapest three days and return the start day and end day index
        lowestPrice = prices[0] + prices[1] + prices[2]
        lowestDays = [0, 2]
        for i in range(len(prices)-2):
            if ((prices[i] + prices[i+1] + prices[i+2]) < lowestPrice):
                lowestPrice = prices[i] + prices[i+1] + prices[i+2]
                lowestDays[0] = i
                lowestDays[1] = i+2
        return lowestDays

