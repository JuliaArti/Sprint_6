import allure
from locators.main_page_locators import LocatorsMain
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import *
from selenium.webdriver.support import expected_conditions


class BasePageScooter:
    def __init__(self, driver):
        self.driver = driver  

    @allure.step('Скролл до элемента')   
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Подождать прогрузки элемента')
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located(locator))  

    @allure.step('Кликнуть элемент')  
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()        

    @allure.step('Ввести назначение в поле ввода')
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys) 

    @allure.step('Получить текст на элемент')
    def get_text_on_element(self, locator):
        return self.driver.find_element(*locator).text            


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
        
    