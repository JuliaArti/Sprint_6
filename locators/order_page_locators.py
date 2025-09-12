from selenium.webdriver.common.by import By

class LocatorsOrder:
    # Поле Имя
    input_field_name = (By.XPATH, '//input[@placeholder="* Имя"]')

    # Поле Фамилия
    input_field_lastname = (By.XPATH, '//input[@placeholder="* Фамилия"]')

    # Поле Адрес: куда привезти заказ
    input_field_address = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')

    # Телефон: на него позвонит курьер
    input_field_phone = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')

    # Поле Станция метро
    input_station_metro = (By.XPATH, '//input[@placeholder="* Станция метро"]')

    # Поле Станция метро
    input_station_metro_name = (By.XPATH, '//button//div[text()="{}"]')

    # Кнопка "Далее"
    button_next = (By.XPATH, "//button[contains(@class, 'utton_Middle__1CSJM')]")

    # Поле Когда привезти самокат
    input_date = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')

    # Поле Срок аренды
    input_rental_period = (By.XPATH, '//div//div[text()="* Срок аренды"]')

    # Срок аренды
    input_rental_period_time = (By.XPATH, '//div[text()="{}"]')

    # Цвет самоката
    color_scooter_name = (By.XPATH, "//label[contains(text(), '{}')]")
  

    # Комментарий для курьера
    comments_courier = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')

    # Кнопка "Заказать"
    button_order = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")

    # Кнопка "Да", подтверждение заказа 
    button_consent = (By.XPATH,  "//button[text()='Да']")    

    # Заказ оформлен
    order_finish = (By.XPATH, "//div[contains(@class, 'Order_Text__2broi')]")