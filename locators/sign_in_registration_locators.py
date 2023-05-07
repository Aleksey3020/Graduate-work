from selenium.webdriver.common.by import By


class SignInRegistrationLocators:
    login_and_register_button = (By.CSS_SELECTOR, '[class="ph-top__menu-link js-open-modal"]')
    register_button1 = (By.CSS_SELECTOR, '[class="rich-form__link btn-link js-replace-modal"]')
    register_button2 = (By.CSS_SELECTOR, '[class="rich-form__submit-btn btn btn--primary btn--wide"]')
    locator_error1_text = (By.CSS_SELECTOR, '[class="form-error-label flc"]')
    locator_email = (By.CSS_SELECTOR, '[class="form__groups flc"] [class="form__group-body"]>div:nth-child(2) input')
    locator_error_email = (By.CSS_SELECTOR, '[class="form__groups flc"] [class="form__group-body"]>div:nth-child(2)'
                                            ' [class="field__input"] div')
    country_selection_button = (By.CSS_SELECTOR, '[class="iti__selected-flag"] ')
    country_code_belarus = (By.XPATH, '//ul[@class="iti__country-list"]//span[2]')
    country_code_kazakhstan = (By.XPATH, '//ul[@class="iti__country-list"]/li[2]//span[2]')
    russia_country_code = (By.XPATH, '//ul[@class="iti__country-list"]/li[5]//span[2]')
    password_5_symbol = (By.CSS_SELECTOR, '[class="form__groups flc"] [class="form__group-body"]>'
                                          'div:nth-child(4) input')
    locator_error_password = (By.CSS_SELECTOR, '[class="form__groups flc"] [class="form__group-body"]>div:nth-child(4) '
                                               '[class="form-error-label flc"]')
    locator_password1_visibility = (By.CSS_SELECTOR, '[class="form__groups flc"] [class="form__group-body"]>'
                                                     'div:nth-child(4) svg:nth-child(2)')
    locator_password2_visibility = (By.CSS_SELECTOR, '[class="form__groups flc"] [class="form__group-body"]>'
                                                     'div:nth-child(5) svg:nth-child(2)')
    authorization_button = (By.CSS_SELECTOR, '[class="rich-form__link btn-link js-replace-modal"]')
    authorization_tab_element = (By.CSS_SELECTOR, '[class="rich-form__title flc"]')
    exit_authorization = (By.CSS_SELECTOR, '[class="modal__window"]>div>div:nth-child(1) '
                                           '[class="modal-panel"]>div:nth-child(1)>button')
