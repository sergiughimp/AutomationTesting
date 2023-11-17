import time
from behave import *

@Given("I am on a Sign In page")
def step_impl(context):
    context.browser.go_to("sign-in")
    time.sleep(2)
@When("I input a valid email")
def step_impl(context):
    valid_email = "ghimpsergiu@gmail.com"
    context.browser.input_email(valid_email)
@When("I input a valid password")
def step_impl(context):
    valid_password = "Password@2023"
    context.browser.input_password(valid_password)
@When("I click the login button")
def step_impl(context):
    context.browser.click_login_button()
@Then("I am still on the Sign In page")
def step_impl(context):
    assert context.browser.get_current_url() == 'https://jules.app/sign-in'


@When("I input a fake email")
def step_impl(context):
    fake_email = "fakeemail@gmail.com"
    context.browser.input_email(fake_email)
@When("I input a fake password")
def step_impl(context):
    valid_password = "Password@20231"
    context.browser.input_password(valid_password)
@Then("I receive '{err_msg}' error message")
def step_impl(context, err_msg):
    assert context.browser.is_error_message_displayed(err_msg)
