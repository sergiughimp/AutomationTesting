from behave import *

@When('I login successfully with "{username}" and "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)

@Then("There are 6 products on the Inventory page")
def step_impl(context):
    assert context.inventory_page.get_products_count() == 6

@Given("I am not log in user")
def step_impl(context):
    pass
@When("I try to go the Inventory Page")
def step_impl(context):
    context.inventory_page.get_page()
@Then("I am redirected to Login Page")
def step_impl(context):
    assert context.browser.get_current_url() == context.login_page.URL
@Then("I receive 'Epic sadface' error message")
def step_impl(context):
    expected_err_msg = "Epic sadface: You can only access '/inventory.html' when you are logged in."
    assert context.login_page.get_error_message() == expected_err_msg

@Given("I am a log in user")
def step_impl(context):
    context.login_page.get_page()
    context.login_page.login("standard_user", "secret_sauce")
@Given("I am on Inventory page")
def step_impl(context):
    context.inventory_page.get_page()
@When("I add a product to cart")
def step_impl(context):
    context.inventory_page.add_product_to_cart()
@Then("The product button changes to remove")
def step_impl(context):
    assert context.inventory_page.remove_product_from_cart_exists()
@Then("The cart is incremented by one")
def step_impl(context):
    assert int(context.inventory_page.get_cart_badge_counter()) == 1