from os import name
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage

scenarios("../features/login.feature")

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@given("the user navigates to the login page")
def open_login_page(login_page):
    login_page.load()

@when(parsers.parse('the user enters email "{email}" and password "{password}"'))
def enter_credentials(login_page, email, password):
    # email and password are provided by the Scenario Outline examples in the .feature file
    login_page.login(email, password)

@when("clicks the login button")
def click_login(login_page):
    # Already clicked in login() method; can pass for this step
    pass

@then("the user should see 'My Account' page")
def verify_login(login_page):
    #login_page.getByRole('link', { name: 'View your order history' })
    #assert login_page.locator('link', { name: 'View your order history' }).text_content() == "View your order history"
    #assert login_page.getByRole('link', { name: 'View your order history' }).text_content() == "My Account"
    pass
