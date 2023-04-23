from selenium.webdriver.common.by import By


class MainPageLocators:
    visible_element1_main_page = (By.CSS_SELECTOR, '[class="ph-main__logo-icon"]>use')
    visible_element2_main_page = (By.XPATH, '//div[@class="ph-top__right"] //li[2]/button')
    email_input_line = (By.CSS_SELECTOR, '[class="text-input-label"]>input')
    subscribe_button = (By.CSS_SELECTOR, '[class="subscription__submit"]')
    email_text_error = (By.CSS_SELECTOR, '[class="form-error-label flc"]')

    feedback = (By.CSS_SELECTOR, '[class="b24-widget-button-icon-container"]')
    text_feedback = (By.CSS_SELECTOR, '[class="b24-form-header-title"]')
    exit_feedback = (By.CSS_SELECTOR, '[class="b24-window-panel b24-window-panel-pos-right"]>button')

    email_in_feedback = (By.CSS_SELECTOR, '[class="b24-form-content b24-form-padding-side"]>form>'
                                          'div:nth-child(1)>div:nth-child(4) input')
    send_button = (By.CSS_SELECTOR, '[class="b24-form-wrapper b24-form-border-bottom"]>div:nth-child(2)>'
                                    'form>div:nth-child(3)>div')
    email_error = (By.CSS_SELECTOR, '[class="b24-form-content b24-form-padding-side"]>form>div>div:nth-child(4) '
                                    '[class="b24-form-control-alert-message"]')

    catalog = (By.XPATH, '//ul[@class="main-nav__l1-main-list"]//li[3]/a')
    country_russia = (By.CSS_SELECTOR, '[class="ph-top__right"]  ul img')
    locator_city = (By.CSS_SELECTOR, '[class="v-geolocation-plain-text geolocation-plain-text"]')
    country_belarus = (By.CSS_SELECTOR, '[class="ph-top__right"]  ul>li a:nth-child(2)>img')