import os
from dotenv import load_dotenv

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage

load_dotenv()

def test_login(page):
    home = HomePage(page)
    login = LoginPage(page)

    home.load()
    home.goto_login()

    login.login(
        os.getenv("USER_EMAIL"),
        os.getenv("USER_PASSWORD")
    )

    assert page.locator("text=Logged in as").is_visible()