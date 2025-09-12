import allure
import pytest
from selenium.webdriver.firefox.webdriver import WebDriver
from urls import *
from data import *
from pages.main_page import MainPageScooter


class TestFAQ:
    @pytest.mark.parametrize("id_question, id_answer, answer_text", [
        ("accordion__heading-0", '//div[@id="accordion__panel-0"]//p', 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        ("accordion__heading-1", '//div[@id="accordion__panel-1"]//p', 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
        ("accordion__heading-2", '//div[@id="accordion__panel-2"]//p', 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        ("accordion__heading-3", '//div[@id="accordion__panel-3"]//p', 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        ("accordion__heading-4", '//div[@id="accordion__panel-4"]//p', 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        ("accordion__heading-5", '//div[@id="accordion__panel-5"]//p', 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
        ("accordion__heading-6", '//div[@id="accordion__panel-6"]//p', 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        ("accordion__heading-7", '//div[@id="accordion__panel-7"]//p', 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    ])

    @allure.title('Проверка раздела "Вопроса о важном"')
    @allure.description('Проверка появления нужного текста  при нажатиина каждую иконку развертывается верный ответ"')
    def test_faq(self, driver: WebDriver, id_question, id_answer, answer_text):
        main_page = MainPageScooter(driver)
        main_page.open_main_page()
        main_page.click_faq_section(id_question) 
        answer_1 = main_page.get_faq_answer_text(id_answer)
                   
        assert answer_text in answer_1