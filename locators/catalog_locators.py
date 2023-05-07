from selenium.webdriver.common.by import By


class CatalogPageLocators:
    element_men = (By.CSS_SELECTOR, '[class="catalog__header-title h2"]')
    checkbox_genuine_leather = (By.CSS_SELECTOR, '[class="check-list flcc check-list--column"] span')
    icon_genuine_leather = (By.CSS_SELECTOR, '[class="catalog-item__header-state-text flc"]>img')
    checkbox_ribbon_belt = (By.XPATH, '//div[@class="catalog-form"]/div[3]/div[2]//div[@class="check-list__grid"]/'
                                      'div[5]//span')
    icon_add_to_favorites = (By.CSS_SELECTOR, '[class="v-favorite-btn favorite-button btn favorite-button--icon"]')