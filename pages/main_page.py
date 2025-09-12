import allure
from locators.main_page_locators import LocatorsMain
from urls import *
from selenium.webdriver.common.by import By
from pages.base_page import BasePageScooter

class MainPageScooter(BasePageScooter):

        
    @allure.step('Кликаем кнопку "Заказать" внизу страницы')
    def click_button_order_down(self):
        

        
        self.wait_visibility_of_element((LocatorsMain.button_order_down))
       
        self.scroll_to_element((LocatorsMain.button_order_down))
        self.click_on_element((LocatorsMain.button_order_down))

    @allure.step('Кликаем на вопрос')   
    def click_faq_section(self, id_question):    
        self.wait_visibility_of_element((By.ID, id_question))
            
        self.scroll_to_element ((By.ID, id_question))
        self.click_on_element((By.ID, id_question))

    @allure.step('Проверяем ответ на вопрос')
    def get_faq_answer_text(self, id_answer):
        
        
        self.wait_visibility_of_element((By.XPATH, id_answer))
        return  self.get_text_on_element((By.XPATH, id_answer))


    @allure.step('Переходим к форме данных клиента при клике на кнопку Заказать вверху страницы')
    def click_button_order_up(self):
        self.click_on_element((LocatorsMain.button_order_up))    

        self.wait_loading_of_url(order_site)


    @allure.step('При клике на лого Самокат совершается переход на главную страницу')        
    def click_title_scooter (self):    
        self.click_on_element((LocatorsMain.title_scooter))
        return  self.wait_loading_of_url(main_site)
        
    
    @allure.step('При клике на лого Яндекс открывается новая вкладка Дзен')
    def click_yandex_logo(self):
        self.click_on_element((LocatorsMain.title_yandex))
        

    @allure.step('Вызов стартовой страницы')    
    def open_main_page(self):
        self.open_url(main_site)