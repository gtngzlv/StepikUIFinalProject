from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    CONTENT_MESSAGE = (By.CSS_SELECTOR, ".content p")
    CONTENT_TABLE = (By.CSS_SELECTOR, "#basket_formset")


class LoginPageLocators:
    EMAIL_INPUT = (By.NAME, "registration-email")
    PASSWORD_INPUT = (By.NAME, "registration-password1")
    REPEAT_PASSWORD_INPUT = (By.NAME, "registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[value='Register']")


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
