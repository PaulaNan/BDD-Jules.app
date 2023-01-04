from pages.sign_in_page import SignInPage
from pages.forgot_pass_page import ForgotPasswordPage
from browser import Browser


def before_all(context):
    context.browser = Browser()
    context.sign_in_page = SignInPage()
    context.forgot_pass_page = ForgotPasswordPage()


def after_all(context):
    context.browser.close()

# the context is like a box that contains a type of object like classes from pages
# every time we add a new page on the project we will add an object in context
