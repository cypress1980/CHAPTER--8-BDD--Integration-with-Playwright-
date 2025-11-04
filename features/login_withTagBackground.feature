@smoke @regression
Feature: Login Functionality

Background:
    Given the user navigates to the login page

  Scenario Outline: User logs in with valid credentials
    When the user enters email "<email>" and password "<password>"
    And clicks the login button

    Examples:
      | email                     | password   |
      | johnpeter123@yopmail.com  | Test@1234  |