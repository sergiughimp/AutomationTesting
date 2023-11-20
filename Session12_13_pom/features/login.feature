Feature: Swag Labs Login Page

  Scenario Outline: Login fail
    Given I am on sign in page
    When I input a "<username>" username
    And I input a "<password>" password
    And I click on Login button
    Then I receive 'Epic sadface' error message

    Examples: Credentials
      | username      | password      |
      | fake_user     | fake_password |
      | standard_user | fake_password |
      | fake_user     | secret_sauce  |

  Scenario: Login success
    Given I am on sign in page
    When I input a "standard_user" username
    And I input a "secret_sauce" password
    And I click on Login button
    Then I am on the Inventory page