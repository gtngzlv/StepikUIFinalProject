from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def content_message_equals_to(self, message):
        content_message = self.browser.find_element(*BasketPageLocators.CONTENT_MESSAGE).text
        assert content_message == message, f"Messages in content basket are not equal to provided {message}"

    def content_with_added_books_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.CONTENT_TABLE), "Content table in basket has " \
                                                                               "something, should be empty "
