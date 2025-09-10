import allure
from locators.main_page_locators import LocatorsMain
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import *
from selenium.webdriver.common.by import By
from pages.base_page import BasePageScooter

class MainPageScooter(BasePageScooter):

    def __init__(self, driver):
        self.driver = driver        
    
    @allure.step('Кликаем кнопку "Заказать" внизу страницы')
    def click_button_order_down(self):
        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LocatorsMain.button_order_down)
        )
        button_order_down = self.driver.find_element(*LocatorsMain.button_order_down)
        self.driver.execute_script("arguments[0].scrollIntoView();", button_order_down) 
        button_order_down.click()
 
    @allure.step('Кликаем на вопрос')   
    def click_faq_section(self, id_question):    
    
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, id_question))
        )
        element = self.driver.find_element(By.ID, id_question)
        self.driver.execute_script("arguments[0].scrollIntoView();", element) 

        how_much = self.driver.find_element(By.ID, id_question)
        how_much.click()

    @allure.step('Проверяем ответ на вопрос')
    def get_faq_answer_text(self, id_answer):
        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, id_answer))
        )
        return  self.driver.find_element(By.XPATH, id_answer)
