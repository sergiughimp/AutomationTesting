from behave import *

@Given("I am on sign in page")
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
@Then("I receive 'Epic sadface' error message")
def step_impl(context):
    expected_error_message = "Epic sadface: Username and password do not match any user in this service"
    assert context.login_page.get_error_message() == expected_error_message

@Then("I am on the Inventory page")
def step_impl(context):
    # check that I am on the current page
    assert context.browser.get_current_url() == context.inventory_page.URL
    # check that the title is right as in the page
    assert context.inventory_page.get_page_title() == "Products"