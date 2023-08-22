from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, "Word 'login' is not in the current URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not on the page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Register form is not on the page"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.com"        
        password = "Fake_fake123"
        email_input = self.browser.find_element(*LoginPageLocators.E_MAIL_INPUT)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)
        password_confirm_input = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_INPUT)
        password_confirm_input.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_button.click()

