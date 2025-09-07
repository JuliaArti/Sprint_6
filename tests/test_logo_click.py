import allure
from selenium.webdriver.firefox.webdriver import WebDriver
from urls import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import *
from pages.base_page import BasePageScooter

class TestPageTransfers:
    
    @allure.title('Проверка переходана на гл страницу при клике на лого Самокат')
    @allure.description('Переход с главной страницы на форму бронирования, клик на лого Самокат')
    def test_scooter(self, driver: WebDriver):
        driver.get(main_site)


        base_page = BasePageScooter(driver)
        base_page.click_button_order_up()
        base_page.click_title_scooter()
        assert WebDriverWait(driver, 10).until(
            EC.url_to_be(main_site)
        )
        
        
        
    @allure.title('Проверка переходана на  страницу Дзен при клике на лого Яндекс')
    @allure.description('Переход с главной страницы  на новую вкладку Дзен')    
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