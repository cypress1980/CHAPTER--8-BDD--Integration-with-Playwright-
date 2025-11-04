import pytest
from pytest_bdd import scenarios, when, then,given, parsers
from pages.search_page import SearchPage
from pages.login_page import LoginPage

#scenarios("../features/search.feature")
scenarios("../features/search_withTagBackground.feature")

@pytest.fixture
def search_page(page):
    return SearchPage(page)


@pytest.fixture
def login_page(page):
    return LoginPage(page)

@given("the user navigates to the login page")
def open_login_page(login_page):
    login_page.load()

@when(parsers.parse('the user enters email "{email}" and password "{password}"'))
def enter_credentials(login_page, email, password):
    login_page.login(email, password)

@when("clicks the login button")
def click_login(login_page):
    login_page.click_login()

@when(parsers.parse('the user searches for text "{text}"'))
def do_search(search_page, text):
    search_page.search(text)

@then(parsers.parse('the search results should display product "{product}"'))
def verify_search(search_page, product):
    assert search_page.is_product_present(product), f"Expected product '{product}' not found in search results"