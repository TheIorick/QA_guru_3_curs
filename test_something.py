from webbrowser import Chrome

import pytest

@pytest.fixture(scope = "session")
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

def test_logout(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"
