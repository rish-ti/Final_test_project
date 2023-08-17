from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):

	def should_be_empty_basket(self):
		assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), "There are items in the basket, but should not be"

	def should_be_message_about_empty_basket(self):
		assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "No empty basket message, but should be"