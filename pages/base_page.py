import allure
from selenium.webdriver.support.wait import WebDriverWait
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


    @allure.step('Ожидание загрузки URL')
    def wait_loading_of_url(self, url):
        return WebDriverWait(self.driver, 6).until(expected_conditions.url_to_be(url))  
    

    @allure.step('Открытие страницы')
    def open_url(self, url):
        self.driver.get(url)


    @allure.step('Переход на другую вкладку')  
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])