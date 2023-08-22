from selenium.webdriver.common.by import By

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	REGISTRATION_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
	E_MAIL_INPUT = (By.CSS_SELECTOR, "input#id_registration-email")
	PASSWORD_INPUT = (By.CSS_SELECTOR, "input#id_registration-password1")
	CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "input#id_registration-password2")
	REG_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
	ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
	BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
	ADDING_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-success strong")
	BOOK_VALUE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
	BASKET_VALUE = (By.CSS_SELECTOR, ".alert.alert-info strong")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-success .alertinner strong")

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	BASKET_LINK = (By.XPATH, '//a[contains(@class, "btn-default") and contains(@href, "/basket/")]')
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")
	
class BasketPageLocators():
	ITEMS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
	EMPTY_BASKET_MESSAGE = (By.XPATH, '//div[@id="content_inner"]/p')
