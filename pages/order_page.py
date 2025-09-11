import allure
from locators.order_page_locators import LocatorsOrder
from urls import *
from pages.base_page import BasePageScooter


class OrderPageScooter(BasePageScooter):

    
    @allure.step('Заполняем форму с данными клиента')
    def fill_customer_form (self, name, lastname, address, station_metro_name, phone):
        
        self.send_keys_to_input((LocatorsOrder.input_field_name),name)
        self.send_keys_to_input((LocatorsOrder.input_field_lastname),lastname)
        self.send_keys_to_input((LocatorsOrder.input_field_address),address)
        self.click_on_element((LocatorsOrder.input_station_metro))
        

        # Выбираем станцию метро
        station_locator = LocatorsOrder.input_station_metro_name
        station_locator = (station_locator[0], station_locator[1].format(station_metro_name))
        
        self.wait_visibility_of_element((station_locator))
        self.click_on_element((station_locator))

        self.send_keys_to_input((LocatorsOrder.input_field_phone),phone)
    
    @allure.step('Нажимаем кнопку Далее')
    def click_button_next(self):
        
        self.click_on_element((LocatorsOrder.button_next))

    @allure.step('Переход на форму бронирования самоката')
    def fill_scooter_form (self,date, rental_period_time, color_scooter_name):    
        
        self.wait_visibility_of_element((LocatorsOrder.input_date))
        
               
        self.click_on_element((LocatorsOrder.input_rental_period))

        # Выбираем срок аренды
        rental_period_locator = (LocatorsOrder.input_rental_period_time[0], LocatorsOrder.input_rental_period_time[1].format(rental_period_time))
        
        self.wait_visibility_of_element((rental_period_locator))
        self.click_on_element((rental_period_locator))
        self.send_keys_to_input((LocatorsOrder.input_date),date)


        color_scooter_locator = (LocatorsOrder.color_scooter_name[0], LocatorsOrder.color_scooter_name[1].format(color_scooter_name))
        
        self.click_on_element((color_scooter_locator))

    @allure.step('Переход на форму подтверждения')
    def click_button_order(self):    

        self.click_on_element((LocatorsOrder.button_order))
        self.wait_visibility_of_element((LocatorsOrder.button_consent))

    @allure.step('Подтверждение заказа')
    def click_button_consent(self):
       
        self.wait_visibility_of_element((LocatorsOrder.button_consent))
        self.click_on_element((LocatorsOrder.button_consent))   

    @allure.step('Проверяем что заказ оформлен')
    def check_order_scooter(self):
    
        return self.wait_visibility_of_element((LocatorsOrder.order_finish))