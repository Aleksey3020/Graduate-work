import time

from page_object.main_page import ShopMainPage
from page_object.catalog_page import ShopCatalogPage
from page_object.exit_and_registration import ExitAndRegistration
from page_object.work_in_personal_account import PersonalAccount


def test_online_store(browser):
# Проверки на главной страницы
    main = ShopMainPage(browser)
    main.open()
# Проверка главной страницы на ожидание
    main.checking_main_page_for_expectation()
# Наличие и кликабельность кнопки связаться с консультантом и наличие надписи обратная связь, выход
    main.feedback_button_test()
# Проверяем наличие ошибки при некорректном вводе email в обратной связи, выход
    main.email_error_checking()
# Проверяем наличие элемента GALANTEYA на главной страницы
    main.check_element1_for_pending()
# Проверяем наличие кнопки Вход/Pегистрация на главной страницы
    main.check_element2_for_pending()
# Проверка на ожидаемость города от выбранной страны Россия
    main.expected_city_of_moscow()
# Проверка на ожидаемость города от выбранной страны Буларусь
    main.expected_city_of_minsk()
# Проверяем наличие ошибки при некорректном вводе email
    main.error_incorrect_email_input()

# Переходим в вкладку каталог интернет магазина
    main.catalog_muzhchinam()
    catalog = ShopCatalogPage(browser)
# Проверка на ожидаемый элемент->мужчинам
    catalog.check_for_expected_element()
# Проверка на наличие иконки->натуральная кожа
    catalog.presence_of_genuine_leather_icon()
# Проверка иконки->добавить в избранное
    catalog.presence_of_the_icon_add_to_favorites()
# Выбераем синтетическая ткань и кликаем на 1 изделие и провераем открылось ли то изделие которое мы кликнули
    catalog.product_conformity_check()
    time.sleep(4)
# Проверка на ожидаемость валюты
    catalog.currency_expectancy_check()
# Проверка материала
    catalog.material()
# Проверка наличия кнопки избранные товары и ее кликабельность, отоюражение количество товара над значком
    catalog.checking_the_favorites_button()
# Проверка наличие товара в избранные товары
    catalog.product_expectancy_check()
# Проверяем кликабельность и текст Добавить в корзину, наличие добавленного товара в корзине
    catalog.check_add_to_cart_button()
# Проверка параметра 'Количество' в корзине
    catalog.checking_quantity_parameter()
# Проверка на совпадение параметра цена с ИТОГО
    catalog.price_match_check()
# Проверка наличие кнопки Перейти к оформлению и ее текст и выходим с корзины
    catalog.check_button_go_to_checkout()

# Переходим
    registration = ExitAndRegistration(browser)
# Проверка наличия ошибки 'Поля обязательное для заполнения'
    registration.check_for_error()
# Проверка наличии ошибки 'Некорректный e-mail'
    registration.email_validation()
# Проверка, на совпадение кодов страны
    registration.checking_country_codes()
# Проверка, на совпадение кодов страны
    registration.checking2_country_codes()
# Проверка наличии ошибки 'Минимум 6 символов'
    registration.symbol_count_check()
# Проверка наличие кнопки видимость пороля и ее кликабельность
    registration.password_visibility_button()
# Проверка кликабельности кнопки 'Авторизация'
    registration.verification_button_authorization()

# Переходим
    personal_account = PersonalAccount(browser)
# Проверка на то, что мы вошли в личный кабинет
    personal_account.checking_personal_account()
# Проверяем изменение цены относительно выбора количество изделий
    personal_account.price_change_check()
# Проверяем кнопки оформить заказ
    personal_account.checking_order_status()
# Проверка строки статус.
    personal_account.check_string_status()
# Проверка кнопки перейти к оплате
    personal_account.checking_the_proceed_to_payment_button()

