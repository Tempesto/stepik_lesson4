from .base_page import BasePage
from .locators.help_function.help_function import HelpFunction


class BasketPage(BasePage):
    def find_element_product_in_basket(self, prod_name, col, tag_name):
        helper = HelpFunction()
        find_row_of_product = helper.find_row_in_table_by_text(prod_name)
        find_price_of_item = self.browser.find_element(
            *helper.find_element_in_row(find_row_of_product[1], col, tag_name))
        return find_price_of_item.text
