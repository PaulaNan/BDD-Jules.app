from browser import Browser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

# in this page we put all that is useful in other pages
# the other pages will inherit this class


class BasePage(Browser, unittest.TestCase):
    def wait_for_element(self, by, selector):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, selector)))
