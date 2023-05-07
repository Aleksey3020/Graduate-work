from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    login_and_register_button = (By.CSS_SELECTOR, '[class="ph-top__menu-link js-open-modal"]')
    email_input = (By.CSS_SELECTOR, '[class="form__group-body"]>div input')
    password_input = (By.CSS_SELECTOR, '[class="form__group-body"]>div:nth-child(2) input')
    login_button = (By.CSS_SELECTOR, '[class="rich-form__action rich-form__action--block"]>button')
    open_personal_account = (By.CSS_SELECTOR, '[class="ph-top__menu-link ph-top__menu-link--dropdown-btn'
                                              ' js-dropdown__btn"]')
    cart_button = (By.CSS_SELECTOR, '[class ="ph-main__right"] > div:nth-child(2) svg')
    go_to_checkout_button = (By.CSS_SELECTOR, '[class="btn btn--lg btn--primary"]')
    plus_button = (By.CSS_SELECTOR, '[class="multiplier"]>button:nth-child(3)')
    locator_price_value = (By.CSS_SELECTOR, '[class="v-price price price--small price--column"]>div'
                                            '>span[class="price__value"]')
    locator_total_payable = (By.CSS_SELECTOR, '[class="shopping-cart__total-info"]>div:nth-child(4) span')
    string_street = (By.CSS_SELECTOR, '[class="form__groups flc"]>div:nth-child(2) [class="form__group-body"]>'
                                      'div:nth-child(3) input')
    string_house = (By.CSS_SELECTOR, '[class="form__groups flc"]>div:nth-child(2)'
                                     ' [class="form__group-body"]>div:nth-child(5) input')
    string_flat = (By.CSS_SELECTOR, '[class="form__groups flc"]>div:nth-child(2)'
                                    ' [class="form__group-body"]>div:nth-child(6) input ')
    payment_method = (By.CSS_SELECTOR, '[class="form__groups flc"]>div:nth-child(3)'
                                       ' [class="radioblock"]>label:nth-child(2) span:nth-child(3)')
    checkout_button = (By.CSS_SELECTOR, '[class="shopping-cart__total-btn btn btn--primary"]')
    locator_your_order = (By.CSS_SELECTOR, '[class="shopping-cart__success-title h1"]')
    locator_string_status = (By.CSS_SELECTOR, '[class="shopping-cart__order-list"]>li:nth-child(2)>div:nth-child(3)')
    locator_go_to_payment = (By.CSS_SELECTOR, '[class="shopping-cart__order-btn btn btn--primary"]')
