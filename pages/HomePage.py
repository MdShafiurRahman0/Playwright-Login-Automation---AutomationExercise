from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.login_btn = page.locator('a[href="/login"]')

    def load(self):
        self.page.goto("https://www.automationexercise.com/")

        
    def goto_login(self):
        self.login_btn.click()