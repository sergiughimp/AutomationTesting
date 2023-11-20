Feature: Inventory Page

  @single
  Scenario: Has 6 products on page
    Given I am on sign in page
    When I log in successfully with "standad_user" and "secret_sauce"
    Then There are 6 products on the Inventory page