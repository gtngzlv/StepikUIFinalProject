from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasketPageLocators:
    CONTENT_MESSAGE = (By.CSS_SELECTOR, ".content p")
    CONTENT_TABLE = (By.CSS_SELECTOR, "#basket_formset")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_TITLE = (By.CSS_SELECTOR, ".product_main > h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    BOOK_ADDED_TO_BASKET = (By.CSS_SELECTOR, ".alert-success:nth-child(1) .alertinner strong")
    BASKET_COST_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")


class MainPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    GO_TO_BASKET = (By.CSS_SELECTOR, ".basket-mini .btn:nth-child(1)")
