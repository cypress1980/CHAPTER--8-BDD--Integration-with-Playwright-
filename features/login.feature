Feature: Login Functionality

  Scenario Outline: User logs in with valid credentials
    Given the user navigates to the login page
    When the user enters email "<email>" and password "<password>"
    And clicks the login button
    Then the user should see 'My Account' page

    Examples:
      | email                     | password   |
      | johnpeter123@yopmail.com  | Test@1234  |