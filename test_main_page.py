from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest


@pytest.mark.login_test
class TestLoginFromMainPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/ru/accounts/login/")
        login_page.open()
        login_page.register_new_user("123@mail.ru", "123")

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
