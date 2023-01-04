from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class ForgotPasswordPage(BasePage):
    EMAIL_INPUT = (By.XPATH, '//input[@placeholder="Enter your email"]')
    SEND_EMAIL_BTN = (By.XPATH, '//span[text()="Send email"]/parent::button')
    EMAIL_ERROR = (By.XPATH, '//p[contains(text(),"email")]')

    def set_email(self, email):
        # that is how we wait the elements
        self.wait_for_element(*self.EMAIL_INPUT)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        sleep(2)

    def click_send_email_btn(self):
        self.driver.find_element(*self.SEND_EMAIL_BTN).click()

    def verify_email_error_msg(self):
        expected = 'Please enter a valid email address!'
        actual = self.driver.find_element(*self.EMAIL_ERROR).text
        self.assertEqual(actual, expected, 'error message is incorrect')
