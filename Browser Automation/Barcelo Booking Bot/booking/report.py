from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class BookingReport:
    def __init__(self, driver:WebDriver, hotels_element:WebElement, adults, rooms):
        self.driver = driver
        self.hotels_element = hotels_element
        self.party = adults
        self.rooms = rooms
        self.hotels = self.hotels_element.find_elements(By.CSS_SELECTOR, 'div[class="result__list-item"]')

    def search(self): #self.hotels has a list of the hotels, go to each hotel and find the price for each person
                      #in the cheapest room. Later update to also find a Volaris plane ticket 
        print(self.findPrice(self.hotels[5]))
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.back()
        self.refilter()

        # for hotel in self.hotels: #for each hotel, click on booking, get redirected, get price, close tab, 
        #                           #go back to first tab, apply filters again (make it one function), 
        #                           #and continue process for every hotel using findPrice on each one
        #     pass
    
    def refilter(self):
        

    def findPrice(self, hotel:WebElement): #working with each invidiual hotel passed into hotel in the main screen
        self.selectCheapestDays(hotel)
        self.selectOccupancy()
        self.signIn(False)
        self.selectRooms()
        return self.pullPrice()

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
            rooms_element = self.driver.find_element(By.CSS_SELECTOR, 'div[class="thumb-cards_products"]') #This part is not necessary to finding the cheapest room, but is necessary if I want the option to pick cheapest vs more expensive options
                                                                        #rooms_element is the overall element that holds the list of rooms
            cheapest_room = rooms_element.find_element(By.ID, 'auto-parent-card-0')
            book_button = cheapest_room.find_element(By.CSS_SELECTOR, 'button[class="btn button_btn button_primary button_sm"]')

            buttonLoaded = False
            while not buttonLoaded:
                try: #First button click fails, but second one works
                    book_button.click()
                    buttonLoaded = True
                    #print("Button click worked with no error")
                except:
                    buttonLoaded = False
                    #print("Button failed, trying again")
                    #print("Button click caused an error so had to do it twice")

            #time.sleep(2) #Wait some time for the page to update before clicking the continue button
            buttonLoaded = False
            while not buttonLoaded:
                try:
                    continue_button = self.driver.find_element(By.CSS_SELECTOR, 'button[class="btn button_btn button_primary button_md button_block"]')
                    continue_button.click()
                    buttonLoaded = True
                except:
                    buttonLoaded = False
            if i != (numRooms-1):
                self.signIn(False)
        

    def signIn(self, account):
        while len(self.driver.window_handles) == 1:
            time.sleep(1)

        self.driver.switch_to.window(self.driver.window_handles[1])
        if account: #sign in to account
            pass
        else: #continue as guest
            close_button = self.driver.find_element(By.CSS_SELECTOR, 'button[class="tingle-modal__close tingle-modal__close-JS"]')
            #close_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="tingle-modal__close tingle-modal__close-JS"]')))
            #close_button.click()
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
        # for room in range(rooms):
        #     roomSize.append(adultsEachRoom)
        #     numAdultsLeft -= adultsEachRoom
            
        if (numAdultsLeft != 0): #TODO: #7 Too many people and not enough rooms will cause an error. Notify user that more rooms will be allocated
            #("Number of adults did not divide evenly. Adults left: ", numAdultsLeft)
            for i in range(numAdultsLeft):
                roomSize[i] += 1
            
        #print("Number of adults in each room:", roomSize)

        #numAdults_element = self.driver.find_element(By.CSS_SELECTOR, 'input[class="input-adult input-JS input-adult-JS tooltip-JS tooltip-full-JS"]')
        #addRoom = self.driver.find_element(By.CSS_SELECTOR, 'div[class="c-cta mod--cta-md mt-4 md:mt-0 mb-5 add-JS"]')
        #addRoom.click()
        #print(numAdults_element.is_displayed())

        for i in range(rooms): #elements may need to be adjusted when a new room is added
            if i != 0: #if it's not the first room, add another room
                addRoom = self.driver.find_element(By.CSS_SELECTOR, 'div[class="c-cta mod--cta-md mt-4 md:mt-0 mb-5 add-JS"]')
                addRoom.click()
            
            #Add the number of adults for each room
            #Bring down the number of adults to one
            numAdults_elements = self.driver.find_elements(By.CSS_SELECTOR, 'input[class="input-adult input-JS input-adult-JS tooltip-JS tooltip-full-JS"]')
            subAdults_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'div[class="c-incrementers__btn dec-button-JS"]')
            addAdults_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'div[class="c-incrementers__btn inc-button-JS"]')

            #print("Adults text size: ", len(numAdults_elements))
            #print("Sub buttons: ", len(subAdults_buttons))
            #print("Add buttons: ", len(addAdults_buttons))

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
        hotelBooking = hotel.find_element(By.CSS_SELECTOR, 'button[class="mod--cta-fullbg mod--cta-full-width mod--cta-color-red booking-button-JS"]')
        
        try:
            loading = self.driver.find_element(By.CSS_SELECTOR, 'div[class="c-loading c-loading-JS bhg-loading mod--loading-active common-transition mod--fullscreen"]')
            while loading.is_displayed():
                time.sleep(1)
                #print("Waited one second for loading screen")
        except:
            pass

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
        #print("Size of days found", len(dates))
        #dates +=  test.find_elements(By.CSS_SELECTOR, '')
        #print(len(dates))
        
        #dates.sort(key=dates.num)
        #time.sleep(5) #Let the calendar load in all elements
        prices = []
        numOfDays = 3 

        for day in dates:
            # wait = WebDriverWait(self.driver, 10)
            # price = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
            #     'span[class="price-day-calendar mod--green-text"], span[class="price-day-calendar mod--yellow-text"], span[class="price-day-calendar mod--red-text"]'
            #     ))).find_element(By.CSS_SELECTOR, #Get the price for that day
            #     'span[class="c-price__value c-price__value-JS"]'
            #     ).get_attribute('innerHTML')
            # prices.append(int(price))
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

            # prices.append(int(day.find_element(By.CSS_SELECTOR, #Get the element for each day
            # 'span[class="price-day-calendar mod--green-text"], span[class="price-day-calendar mod--yellow-text"], span[class="price-day-calendar mod--red-text"]'
            # ).find_element(By.CSS_SELECTOR, #Get the price for that day
            # 'span[class="c-price__value c-price__value-JS"]'
            # ).get_attribute('innerHTML')))

        #print(prices)
        cheapest = self.findCheapestDays(prices)
        #print(cheapest)

        #print("Cheapest and soonest days are:", cheapest[0], cheapest[1])
        dates[cheapest[0]].click() #start day
        dates[cheapest[1]].click() #end day


    def findCheapestDays(self, prices): #Find the cheapest three days and return the start day and end day index
        lowestPrice = prices[0] + prices[1] + prices[2]
        #print("Lowest price: ", lowestPrice)
        lowestDays = [0, 2]
        for i in range(len(prices)-2):
            if ((prices[i] + prices[i+1] + prices[i+2]) < lowestPrice):
                lowestPrice = prices[i] + prices[i+1] + prices[i+2]
                #print("Lowest price: ", lowestPrice)
                lowestDays[0] = i
                lowestDays[1] = i+2
        return lowestDays

