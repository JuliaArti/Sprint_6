import pytest
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import *
from urls import *
from pages.main_page import MainPageScooter
from pages.order_page import OrderPageScooter
from pages.base_page import BasePageScooter



class TestOrderScooter:

    @pytest.mark.parametrize("name, lastname, address, station_metro_name, phone, date, rental_period_time, color_scooter_name", [
        (name_1, lastname_1, address_1, metro_station_1, phone_number_1, date_1, rental_period_time_1, color_scooter_1),
        (name_2, lastname_2, address_2, metro_station_2, phone_number_2, date_2, rental_period_time_2, color_scooter_2)

    ])

    # Открываем стартовую страницу и кликаем кнопку "Заказать" в верху страницы
    def test_start_page_and_order_up(self, driver: WebDriver, name, lastname, address, station_metro_name, phone, date, rental_period_time, color_scooter_name):
        driver.get(main_site)

        base_page = BasePageScooter(driver)
        base_page.click_button_order_up()


        # Заполняем форму заказа
        order_page = OrderPageScooter(driver)
        order_page.fill_customer_form(name, lastname, address, station_metro_name, phone)
        order_page.click_button_next()
        order_page.fill_scooter_form(date, rental_period_time, color_scooter_name)
        order_page.click_button_order()
        order_page.click_button_consent()
        assert order_page.check_order_scooter()
        
    

    # Открываем стартовую страницу и кликаем кнопку "Заказать" внизу страницы
    def test_start_page_and_order_down(self, driver: WebDriver):
        driver.get(main_site)
        
        main_page = MainPageScooter(driver)
        main_page.click_button_order_down()
     
        assert WebDriverWait(driver, 10).until(
            EC.url_to_be(order_site)
        )