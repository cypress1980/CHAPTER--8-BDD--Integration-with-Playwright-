from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("input#input-email")
        self.password_input = page.locator("input#input-password")
        self.login_btn = page.locator("input[type='submit']")

    def load(self):
        self.page.goto("https://naveenautomationlabs.com/opencart/index.php?route=account/login")

    def login(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        
    def click_login(self):
        self.login_btn.click()