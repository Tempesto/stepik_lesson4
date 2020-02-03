from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest
import time

# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"


@pytest.mark.parametrize('link', ["0", "1", "2", "3", "4", "5", "6",
                                  pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, f"{link2}{link}")
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    prod_name = page.get_name_of_product()
    prod_price = page.get_price_of_product()
    alert_text = page.get_text_in_alert_add_to_basket()
    print("prod_name = ", prod_name, " alert name = ", alert_text)
    assert prod_name == alert_text, "The product that was added to the cart does not match the message about adding to " \
                                    "the cart."
    page.click_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    prod_price_in_basket = basket_page.find_element_product_in_basket(prod_name, 4, "p")
    prod_name_in_basket = basket_page.find_element_product_in_basket(prod_name, 2, "a")
    print("prod price = ", prod_price, " = ", prod_price_in_basket)
    print("prod_name = ", prod_name, " = ", prod_name_in_basket)
    # time.sleep(5)
    assert prod_price == prod_price_in_basket
    assert prod_name == prod_name_in_basket, "Not elements"
