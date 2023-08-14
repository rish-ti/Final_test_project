from .pages.product_page import ProductPage
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.parametrize('number', ["0",
                                  "1",
                                  "2",
                                  "3",
                                  "4",
                                  "5",
                                  "6",
                                  pytest.param("7", marks=pytest.mark.xfail),
                                  "8",
                                  "9"])

def  test_guest_can_add_product_to_basket(browser, number):
	link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
	page = ProductPage(browser, link)
	page.open()
	page.add_product_to_basket()
	page.solve_quiz_and_get_code()
	page.certain_book_should_be_added_to_basket()
	page.should_be_certain_value_of_basket()