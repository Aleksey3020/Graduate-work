from selenium.webdriver.common.by import By


class OpenGoodsLocators:
    checkbox_genuine_leather = (By.CSS_SELECTOR, '[class="check-list flcc check-list--column"] span')
    product = (By.CSS_SELECTOR, '[class="catalog__wrapper"]>div>a')
    locator_open_product = (By.CSS_SELECTOR, '[class="product-card__row"]>div:nth-child(1)')
    mani = (By.CSS_SELECTOR, '[class="product-card__cell-main"]>div:nth-child(2) span:nth-child(2)')
    material = (By.CSS_SELECTOR, '[class="product-card__specifications-list"]>li')
    favorites_button = (By.CSS_SELECTOR, '[class="v-favorite-btn favorite-button btn favorite-button--alt"]')
    quantity_of_selected_item = (By.CSS_SELECTOR, '[class="ph-main"] [class="ph-main__right"] a div')
    open_favorites = (By.CSS_SELECTOR, '[class="header-button__icon"]')
    product_availability = (By.CSS_SELECTOR, '[class="catalog__header-quantity"]')
    locator_exit = (By.CSS_SELECTOR, '[class="v-catalog-item catalog-item catalog-item--alt"]>a')
