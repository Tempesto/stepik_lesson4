from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest
from .pages.locators.base_page_locators import BasePageLocators
from .pages.locators.main_page_locator import MainPageLocators
from .pages.locators.product_page_locator import ProductPageLocator

link = 'http://selenium1py.pythonanywhere.com/'
link_product = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_go_to_login_page(self, browser):
        page = MainPage(browser,
                        link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)  # выполняем метод страницы - переходим на страницу логина
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        assert page.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_the_presence_of_the_inscription_empty_basket()
    text_value = basket_page.text_basket_empty()
    basket_page.is_element_present(*ProductPageLocator.GET_ALERT_ABOUT_PROTUCT_ADD_TO_BASKET)
    assert "Your basket is empty." in text_value, "Text not present in basket"


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link_product)
    page.open()
    page.click_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_the_presence_of_the_inscription_empty_basket()
    text_value = basket_page.text_basket_empty()
    basket_page.is_element_present(*ProductPageLocator.GET_ALERT_ABOUT_PROTUCT_ADD_TO_BASKET)
    assert "Your basket is empty." in text_value, "Text not present in basket"
