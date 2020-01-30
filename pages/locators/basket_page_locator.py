from selenium.webdriver.common.by import By


class BasketPageLocator():
    FIND_PRODUCT = (By.CSS_SELECTOR, "div h3 > a")
    PRISE_OF_ITEM_ADDED_TO_BASKET = (By.XPATH, "//div[@class='row']/div/h3/a[text()='The shellcoder\'s handbook']/"
                                               "ancestor::div/div[@class='col-sm-1']/p[@class='price_color align-right']")
    # def findRowElementInTableByText(self, text):
    #     return By.XPATH, f"//*[text()={text}]/ancestor::row']"
    #
    #
    # findRowElementInTableByText('some')
    #
    # def findValuInRow(self, row, column_number):
    #     return row.browser.find_element()