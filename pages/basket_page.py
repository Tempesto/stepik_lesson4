from .base_page import BasePage
from .locators.help_function.help_function import HelpFunction
from .locators.basket_page_locator import BasketPageLocator


class BasketPage(BasePage):
    def find_element_product_in_basket(self, prod_name, col, tag_name):
        helper = HelpFunction()
        find_row_of_product = helper.find_row_in_table_by_text(prod_name)
        find_price_of_item = self.browser.find_element(
            *helper.find_element_in_row(find_row_of_product[1], col, tag_name))
        return find_price_of_item.text

    def check_the_presence_of_the_inscription_empty_basket(self):
        self.is_element_present(*BasketPageLocator.LINK_YOUR_BASKET_IS_EMPTY)

    def text_basket_empty(self):
        return self.browser.find_element(*BasketPageLocator.LINK_YOUR_BASKET_IS_EMPTY).text
