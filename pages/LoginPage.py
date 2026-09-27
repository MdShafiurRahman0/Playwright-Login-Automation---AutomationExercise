from playwright.sync_api import Page

class LoginPage:
    def __init__(self,page:Page):
        self.email = page.locator('input[data-qa="login-email"]')
        self.password = page.locator('input[data-qa="login-password"]')
        self.login_btn = page.locator('button[data-qa="login-button"]')

    def login(self,email:str,password:str):
        self.email.fill(email)
        self.password.fill(password)
        self.login_btn.click()
