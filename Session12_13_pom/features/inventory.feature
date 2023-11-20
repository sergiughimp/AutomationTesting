Feature: Inventory Page

#  @single
  Scenario: Has 6 products on page
    Given I am on the Sign in page
    When I login successfully with "standard_user" and "secret_sauce"
    Then There are 6 products on the Inventory page

#  @single
  Scenario: Redirect to Login Page when unauthenticated user
    Given I am not log in user
    When I try to go the Inventory Page
    Then I am redirected to Login Page
    And I receive 'Epic sadface' error message

  @single
  Scenario: Add object to cart
    Given I am a log in user
    And I am on Inventory page
    When I add a product to cart
    Then The product button changes to remove
    And The cart is incremented by one
