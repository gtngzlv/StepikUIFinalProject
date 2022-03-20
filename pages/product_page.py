from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_basket_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def return_book_title(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text

    def return_book_price(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text

    def success_messages_presented(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_ADDED_TO_BASKET), "Success message of book was added " \
                                                                                "was not presented "
        assert self.is_element_present(*ProductPageLocators.BASKET_COST_MESSAGE), "Basket cost message was not presented"

    def is_book_title_presented_in_message(self, book_title):
        assert book_title == self.browser.find_element(*ProductPageLocators.BOOK_ADDED_TO_BASKET).text, "Incorrect book title in success message"

    def is_basket_cost_equals_book_cost(self, book_cost):
        assert book_cost in self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text, f"Incorrect book cost, should be {book_cost}"

    def book_added_message_is_not_presented(self):
        assert self.is_not_element_present(*ProductPageLocators.BOOK_ADDED_TO_BASKET), "Success message is presented"

    def book_added_messsage_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.BOOK_ADDED_TO_BASKET), "Book added message still presented on the page"

