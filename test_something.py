from webbrowser import Chrome

import pytest

@pytest.fixture
def browser():
    print("Browser!")

    yield

    print ("Browser closed.")


@pytest.fixture
def user():
    print("User!")
    return "username", "password"


@pytest.fixture
def login_page(browser):
    print("Login page!")
    pass


def test_login(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"