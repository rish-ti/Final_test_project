from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By


def test_guest_is_at_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()