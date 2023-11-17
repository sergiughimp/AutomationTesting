from behave import *

@given("we have behave installed")
def step_imp(context):
    pass

@when("we implement a test")
def step_imp(context):
    assert 1 + 1 == 2

@then("behave will test it for us!")
def step_imp(context):
    assert context.failed is False
