from .base_page import BasePage
from .locators.product_page_locator import ProductPageLocator


class ProductPage(BasePage):

    def add_product_to_cart(self):
        basket = self.browser.find_element(*ProductPageLocator.GET_LINK_ADD_TO_BASKET)
        basket.click()

    def get_name_of_product(self):
        product_name = self.browser.find_element(*ProductPageLocator.GET_PRODUCT_NAME)
        product_text = product_name.text
        return product_text

    def click_to_basket(self):
        self.browser.find_element(*ProductPageLocator.GET_BASKET_LINK).click()

    def get_text_in_alert_add_to_basket(self):
        return self.browser.find_element(*ProductPageLocator.GET_ALERT_ABOUT_PROTUCT_ADD_TO_BASKET).text

    def get_price_of_product(self):
        return self.browser.find_element(*ProductPageLocator.GET_PRICE_OF_PRODUCT_LINK).text
