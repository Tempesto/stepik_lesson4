from .base_page import BasePage
from .locators.main_page_locator import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)
        # alert = self.browser.switch_to.alert
        # alert.accept()
        return MainPage

    def get_be_login_link(self):
        return self.is_element_present(*MainPageLocators.LOGIN_LINK)
