from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def check_names_matching(self):
        product_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        message_title = self.browser.find_element(*ProductPageLocators.TITLE_IN_FIRST_MESSAGE).text
        assert product_title == message_title, "Title is not matched"

    def check_price_matching(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_IN_BOOK_DETAILS).text
        message_price = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text
        assert product_price == message_price, "Price is not matched"


