from selenium.webdriver.common.by import By


class CatalogPageLocators:
    element_men = (By.CSS_SELECTOR, '[class="catalog__header-title h2"]')
    checkbox_genuine_leather = (By.CSS_SELECTOR, '[class="check-list flcc check-list--column"] span')
    icon_genuine_leather = (By.CSS_SELECTOR, '[class="catalog-item__header-state-text flc"]>img')
    checkbox_ribbon_belt = (By.XPATH, '//div[@class="catalog-form"]/div[3]/div[2]//div[@class="check-list__grid"]/'
                                      'div[5]//span')
    icon_add_to_favorites = (By.CSS_SELECTOR, '[class="v-favorite-btn favorite-button btn favorite-button--icon"]')
    product = (By.CSS_SELECTOR, '[class="catalog__wrapper"]>div>a')
    locator_open_product_name = (By.CSS_SELECTOR, '[class="product-card__name h3 hidden-xs"]')
    mani = (By.CSS_SELECTOR, '[class="product-card__cell-main"]>div:nth-child(2) span:nth-child(2)')
    material = (By.CSS_SELECTOR, '[class="product-card__specifications-list"]>li')
    favorites_button = (By.CSS_SELECTOR, '[class="v-favorite-btn favorite-button btn favorite-button--alt"]')
    quantity_of_selected_item = (By.CSS_SELECTOR, '[class="ph-main"] [class="ph-main__right"] a div')
    open_favorites = (By.CSS_SELECTOR, '[class="header-button__icon"]')
    product_availability = (By.CSS_SELECTOR, '[class="catalog__header-quantity"]')
    locator_exit = (By.CSS_SELECTOR, '[class="v-catalog-item catalog-item catalog-item--alt"]>a')
    add_to_cart_button = (By.CSS_SELECTOR, '[class="product-card__btn-add btn btn--lg btn--primary"]')
    text_button = (By.CSS_SELECTOR, '[class="product-card__btn-add-text"]')
    item_in_cart = (By.CSS_SELECTOR, '[class="panel-header__count"]')
    amount = (By.XPATH, '//div[@class="catalog-item-horizontal__info"]/div[5]/span[2]')
    locator_price = (By.CSS_SELECTOR, '[class="catalog-item-horizontal__info"]>div:nth-child(7) span')
    locator_in_total = (By.XPATH, '//div[@class="modal-panel js-v-scope"]/div/div[3]//span')
    go_to_checkout_button = (By.CSS_SELECTOR, '[class="btn btn--lg btn--primary"]')
    cart_exit = (By.CSS_SELECTOR, '[class="v-small-basket-list small-basket-list"] svg>use')
