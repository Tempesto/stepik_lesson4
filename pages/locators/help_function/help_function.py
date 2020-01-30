from selenium.webdriver.common.by import By


class HelpFunction():
    def find_row_in_table_by_text(self, prod_name):
        return By.XPATH, f'//*[text()="{prod_name}"]/ancestor::div[@class="row"]'

    def find_element_in_row(self, row, col, tag_name):
        element_of_item = (By.XPATH, f'{row}' + f'/child::div[{col}]//{tag_name}')
        return element_of_item
