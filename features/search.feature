Feature: Login and Product Search

  Scenario Outline: User logs in with valid credentials
    Given the user navigates to the login page
    When the user enters email "<email>" and password "<password>"
    And clicks the login button
    When the user searches for text "iMac"  
    Then the search results should display product "iMac"

    Examples:
      | email                     | password   |
      | johnpeter123@yopmail.com  | Test@1234  |