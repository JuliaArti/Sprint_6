import allure
from selenium.webdriver.firefox.webdriver import WebDriver
from urls import *
from data import *
from pages.main_page import MainPageScooter

class TestPageTransfers:
    
    @allure.title('Проверка переходана на гл страницу при клике на лого Самокат')
    @allure.description('Переход с главной страницы на форму бронирования, клик на лого Самокат')
    def test_scooter(self, driver: WebDriver):
       
        main_page = MainPageScooter(driver)
        main_page.open_main_page()
        main_page.click_button_order_up()
        main_page.click_title_scooter()
        assert main_page.wait_loading_of_url(main_site)
        
                
    @allure.title('Проверка переходана на  страницу Дзен при клике на лого Яндекс')
    @allure.description('Переход с главной страницы  на новую вкладку Дзен')    
    def test_yandex(self, driver: WebDriver):
             
        main_page = MainPageScooter(driver)
        main_page.open_main_page()
        main_page.click_yandex_logo()

           
        # Переключаемся на новую вкладку
        main_page.switch_to_next_tab()

        assert main_page.wait_loading_of_url(ya_dzen)
        