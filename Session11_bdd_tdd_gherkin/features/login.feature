Feature: Jules Sign In

  Scenario: Successful sign in with valid email and password
    Given I am on a Sign In page
    When I input a valid email
    And I input a valid password
    And I click the login button
    Then I receive 'Invalid email/password combination' error message
    And I am still on the Sign In page

  Scenario: Fail sign in with fake email and password
    Given I am on a Sign In page
    When I input a fake email
    And I input a fake password
    And I click the login button
    Then I am still on the Sign In page

#  Scenario: Fail sign in with fake email and password
#    Given I am on a Sign In page
#    And I input a valid email
#    And I input a valid password
#    And I click the login button
#    Then I receive 'Invalid email/password combination' error message
#    And I am still on the Sign In page

