from .base_page import BasePage
from .locators.login_page_locator import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url_login = self.browser.current_url
        if "login" in url_login:
            login = "login"
        assert login == "login", "Current url is not"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"
        assert True

    def register_new_user(self, email, password):
        enter_email = self.browser.find_element(*LoginPageLocators.INPUT_EMAIL)
        enter_email.send_keys(email)
        enter_pass = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD)
        enter_pass.send_keys(password)
        enter_pass_confirm = self.browser.find_element(*LoginPageLocators.INPUT_CONFIRM_PASSWORD)
        enter_pass_confirm.send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER).click()

