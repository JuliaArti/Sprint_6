from selenium.webdriver.common.by import By
from locators.order_page_locators import LocatorsOrder
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import *


class OrderPageScooter:

    def __init__(self, driver):
        self.driver = driver  

    def fill_customer_form (self, name, lastname, address, station_metro_name, phone):
        # Заполняем форму заказа
        name_field = self.driver.find_element(*LocatorsOrder.input_field_name)
        lastname_field = self.driver.find_element(*LocatorsOrder.input_field_lastname)
        address_field = self.driver.find_element(*LocatorsOrder.input_field_address)
        station_metro = self.driver.find_element(*LocatorsOrder.input_station_metro)
        phone_field = self.driver.find_element(*LocatorsOrder.input_field_phone)
              

        name_field.send_keys(name)
        lastname_field.send_keys(lastname)
        address_field.send_keys(address)
        station_metro.click()

        # Выбираем станцию метро
        station_locator = LocatorsOrder.input_station_metro_name
        station_locator = (station_locator[0], station_locator[1].format(station_metro_name))
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(station_locator)
        )
        station_button = self.driver.find_element(*station_locator)
        station_button.click()

        phone_field.send_keys(phone)
    
    
    def click_button_next(self):
        
        button_next = self.driver.find_element(*LocatorsOrder.button_next)
        button_next.click()

    
    def fill_scooter_form (self,date, rental_period_time, color_scooter_name):    
        # Переходим на вторую часть формы заказа
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LocatorsOrder.input_date)
        )
        input_date = self.driver.find_element(*LocatorsOrder.input_date)
        input_rental_period = self.driver.find_element(*LocatorsOrder.input_rental_period)
       
        input_rental_period.click()

        # Выбираем срок аренды
        rental_period_locator = (LocatorsOrder.input_rental_period_time[0], LocatorsOrder.input_rental_period_time[1].format(rental_period_time))
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(rental_period_locator)
        )
        input_rental_period_four_days = self.driver.find_element(*rental_period_locator)
        input_rental_period_four_days.click()
        input_date.send_keys(date)


        color_scooter_locator = (LocatorsOrder.color_scooter_name[0], LocatorsOrder.color_scooter_name[1].format(color_scooter_name))
        color_scooter_black = self.driver.find_element(*color_scooter_locator)

        color_scooter_black.click()


    def click_button_order(self):    

        button_order = self.driver.find_element(*LocatorsOrder.button_order)
        button_order.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LocatorsOrder.button_consent)
        )


    def click_button_consent(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LocatorsOrder.button_consent)
        )
        button_consent = self.driver.find_element(*LocatorsOrder.button_consent)
        button_consent.click()    


    def check_order_scooter(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LocatorsOrder.order_finish)
        )    