from behave import *

# given - sets initial situation
# when - steps from test
# then - verify from test


@given('sign_in: I am a user on jules sign in page')
def step_impl(context):
    context.sign_in_page.navigate_sign_in_page()


@when('sign_in: I set my email "{email}"')
def step_impl(context, email):
    context.sign_in_page.set_email(email)


@when('sign_in: I set my password "{password}"')
def step_impl(context, password):
    context.sign_in_page.set_pass(password)


@when('sign_in: I click sign in button')
def step_impl(context):
    context.sign_in_page.click_login_button()


@when('sign_in: I click on forgot password link')
def step_impl(context):
    context.sign_in_page.click_forgot_pass_link()
