Feature: Login Page herokuapp
  Scenario: Login success
    Given I am on Login Page
    When I input a "tomsmith" username
    And I input a "SuperSecretPassword!" password
    And I click on Login button
    Then I am on the Secure page