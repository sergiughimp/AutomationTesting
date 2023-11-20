from behave import *
@Given("I am on Home Page")
def step_impl(context):
    context.home_page.get_page()
@When('I click on "Form Authentication" button')
def step_impl(context):
    context.home_page.click_form_authentication_button()

@Then('I am on the Login Page')
def step_impl(context):
    context.login_page.get_page()