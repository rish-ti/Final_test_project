from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def certain_book_should_be_added_to_basket(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        adding_message = self.browser.find_element(*ProductPageLocators.ADDING_MESSAGE).text
        assert book_name == adding_message, "The name of the book is not in the adding message"

    def should_be_certain_value_of_basket(self):
        book_value = self.browser.find_element(*ProductPageLocators.BOOK_VALUE).text
        basket_value = self.browser.find_element(*ProductPageLocators.BASKET_VALUE).text
        assert book_value == basket_value, "The value of the book is not even the value of the basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is still presented, but should have disappeared"






