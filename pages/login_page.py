from .base_page import BasePage
import pytest
import faker
from .locators import MainPageLocators, LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_INPUT).send_keys(password)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "It is not login url"

    def should_be_login_form(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*MainPageLocators.REGISTER_FORM), "Register form is not here"

