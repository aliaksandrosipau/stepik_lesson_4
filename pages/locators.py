from selenium.webdriver.common.by import By


class MainPageLocators():
    pass

class LoginPageLocators():
    # LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    # REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    pass

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    BOOK_TITLE = (By.XPATH, '//div[@class="row"]/div/h1')
    TITLE_IN_FIRST_MESSAGE = (By.XPATH, '//div[@class="alertinner "]/strong')
    PRICE_IN_BOOK_DETAILS = (By.XPATH, '//p[@class="price_color"]')
    PRICE_IN_MESSAGE = (By.XPATH, '//div[@class="alertinner "]/p/strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
