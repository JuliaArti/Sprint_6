#import pytest
#from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from urls import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
#from locators.order_page_locators import LocatorsOrder

#from selenium.webdriver.common.by import By
#from data import Credential 
from data import *
from pages.base_page import BasePageScooter

# @pytest.fixture
# def driver():
#     driver = webdriver.Firefox()
#     driver.maximize_window()
#     yield driver
#     driver.quit()

#class TestLogo:
#     @allure.title('Проверка переходана на гл страницу при клике на лого "Самокат"')
#     def test_logo_main_page(self, driver):
#         main_page = MainPage(driver)
#         main_page.wait_visibility_of_order_button_in_header()
#         main_page.click_on_order_button_up() # button_in_header
#         main_page.wait_visibility_of_title_scooter() #header_logo_scooter
#         main_page.wait_visibility_of_main_header()
#         assert main_page.check_displaying_of_main_header()







class TestPageTransfers:
    
    def test_scooter(self, driver: WebDriver):
        driver.get(main_site)


        base_page = BasePageScooter(driver)
        base_page.click_button_order_up()
        base_page.click_title_scooter()
        assert WebDriverWait(driver, 10).until(
            EC.url_to_be(main_site)
        )
        
        
        
        
    def test_yandex(self, driver: WebDriver):
        driver.get(main_site)
        
        base_page = BasePageScooter(driver)
        base_page.click_yandex_logo()

           
        # Ждем открытия новой вкладки
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        # Переключаемся на новую вкладку
        driver.switch_to.window(driver.window_handles[-1])

        assert WebDriverWait(driver, 10).until(
            EC.url_contains(ya_dzen)
        )