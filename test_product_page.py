import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import time

link = 'http://selenium1py.pythonanywhere.com/'
link_product = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"



def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.go_to_login_page()
        self.page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        self.page.register_new_user(email, "Op000000000!")
        self.page.should_be_autorized_user()

    def test_user_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = ProductPage(browser, browser.current_url)
        page.click_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.check_the_presence_of_the_inscription_empty_basket()
        text_value = basket_page.text_basket_empty()
        assert "Your basket is empty." in text_value, "Text not present in basket"

    def test_user_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, browser.current_url)
        page.click_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.check_the_presence_of_the_inscription_empty_basket()
        text_value = basket_page.text_basket_empty()
        assert "Your basket is empty." in text_value, "Text not present in basket"
