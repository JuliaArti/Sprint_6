from selenium.webdriver.common.by import By

class LocatorsMain:

    # Кнопка "Заказать" в верху страницы
    button_order_up = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g')]" ) 

    # Кнопка "Заказать" внизу страницы
    button_order_down = (By.XPATH, "//button[contains(@class, 'Button_UltraBig__UU3Lp')]")

    # Надпись "Самокат"
    title_scooter= (By.XPATH, "//a[contains(@class, 'Header_LogoScooter__3lsAR')]")

    # Надпись "Яндекс"
    title_yandex = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex__3TSOI')]")
    
    # Вопрос "Сколько это стоит? И как оплатить?"
    how_much = (By.ID, "accordion__heading-0") 
    
    # Ответ на вопрос HM
    answer_1 = (By.XPATH, '//div[@id="accordion__panel-0"]//p')

    #

    #

    #

    #

#

#

#

#

#

#

#

#

#