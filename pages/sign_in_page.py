from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    EMAIL_INPUT = (By.XPATH, '//input[@placeholder="Enter your email"]')
    PASS_INPUT = (By.XPATH, '//input[@placeholder="Enter your password"]')
    LOGIN_BUTTON = (By.XPATH, '//span[text()="Log in"]/parent::button')
    FORGOT_PASS_LINK = (By.XPATH, '//a[text()="Forgot password?"]')

    def navigate_sign_in_page(self):
        self.driver.get('https://jules.app/sign-in')

    # step (the smallest action on a page)
    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def set_pass(self, password):
        self.driver.find_element(*self.PASS_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    # step definition - many little steps under one function
    def user_login(self, email, password):
        self.set_email(email)
        self.set_pass(password)
        self.click_login_button()

    def click_forgot_pass_link(self):
        self.driver.find_element(*self.FORGOT_PASS_LINK).click()

