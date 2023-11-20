from behave import *
@Given('I am on Login Page')
def step_impl(context):
    context.login_page.get_page()
@When('I input a "{username}" username')
def step_impl(context, username):
    context.login_page.input_username(username)
@When('I input a "{password}" password')
def step_impl(context, password):
    context.login_page.input_password(password)
@When("I click on Login button")
def step_impl(context):
    context.login_page.click_login_button()
@Then('I am on the Secure page')
def step_impl(context):
    context.secure_page.get_page_title()
