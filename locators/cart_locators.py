from selenium.webdriver.common.by import By


class CartLocators:
    add_to_cart_button = (By.CSS_SELECTOR, '[class="product-card__btn-add btn btn--lg btn--primary"]')
    text_button = (By.CSS_SELECTOR, '[class="product-card__btn-add-text"]')
    item_in_cart = (By.CSS_SELECTOR, '[class="panel-header__count"]')
    amount = (By.XPATH, '//div[@class="catalog-item-horizontal__info"]/div[5]/span[2]')
    locator_price = (By.CSS_SELECTOR, '[class="catalog-item-horizontal__info"]>div:nth-child(7) span')
    locator_in_total = (By.XPATH, '//div[@class="modal-panel js-v-scope"]/div/div[3]//span')
    go_to_checkout_button = (By.CSS_SELECTOR, '[class="btn btn--lg btn--primary"]')
    cart_exit = (By.CSS_SELECTOR, '[class="v-small-basket-list small-basket-list"] svg>use')
