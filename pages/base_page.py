import allure
from locators.main_page_locators import LocatorsMain
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import *


class BasePageScooter:
    def __init__(self, driver):
        self.driver = driver  

    @allure.step('Переходим к форме данных клиента при клике на кнопку Заказать вверху страницы')
    def click_button_order_up(self):
        button_order_up = self.driver.find_element(*LocatorsMain.button_order_up)
        button_order_up.click()    
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(order_site)
        )


    @allure.step('При клике на лого Самокат совершается переход на главную страницу')        
    def click_title_scooter (self):    
        title_scooter = self.driver.find_element(*LocatorsMain.title_scooter)
        title_scooter.click()
        return  WebDriverWait(self.driver, 10).until(
            EC.url_to_be(main_site)
        )
    
    @allure.step('При клике на лого Яндекс открывается новая вкладка Дзен')
    def click_yandex_logo(self):
        title_yandex = self.driver.find_element(*LocatorsMain.title_yandex)
        title_yandex.click()
        
    