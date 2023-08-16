from selenium.webdriver.common.by import By

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	REGISTRATION_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
	ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
	BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
	ADDING_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-success strong")
	BOOK_VALUE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
	BASKET_VALUE = (By.CSS_SELECTOR, ".alert.alert-info strong")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-success .alertinner strong")

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	