import pytest

from .pages.locators.product_page_locator import ProductPageLocator
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import time


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    prod_name = page.get_name_of_product()
    prod_price = page.get_price_of_product()
    alert_text = page.get_text_in_alert_add_to_basket()
    assert prod_name == alert_text, "The product that was added to the cart does not match the message about adding to " \
                                    "the cart."
    page.click_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    prod_price_in_basket = basket_page.find_element_product_in_basket(prod_name, 4, "p")
    prod_name_in_basket = basket_page.find_element_product_in_basket(prod_name, 2, "a")
    assert prod_price == prod_price_in_basket
    assert prod_name == prod_name_in_basket, "Not elements"


@pytest.mark.need_review
def test_user_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    prod_name = page.get_name_of_product()
    prod_price = page.get_price_of_product()
    alert_text = page.get_text_in_alert_add_to_basket()
    assert prod_name == alert_text, "The product that was added to the cart does not match the message about adding to " \
                                    "the cart."
    page.click_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    prod_price_in_basket = basket_page.find_element_product_in_basket(prod_name, 4, "p")
    prod_name_in_basket = basket_page.find_element_product_in_basket(prod_name, 2, "a")
    assert prod_price == prod_price_in_basket
    assert prod_name == prod_name_in_basket, "Not elements"


def test_guest_should_see_login_link_on_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/'
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.go_to_login_page()
        self.page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        self.page.register_new_user(email, "Op000000000!")
        self.page.should_be_authorized_user()

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


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link_product = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link_product)
    page.open()
    page.click_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_the_presence_of_the_inscription_empty_basket()
    text_value = basket_page.text_basket_empty()
    basket_page.is_element_present(*ProductPageLocator.GET_ALERT_ABOUT_PROTUCT_ADD_TO_BASKET)
    assert "Your basket is empty." in text_value, "Text not present in basket"
