from browser import Browser
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.secure_page import SecurePage
def before_scenario(context, scenario):
    context.browser = Browser()
    context.home_page = HomePage(context.browser)
    context.login_page = LoginPage(context.browser)
    context.secure_page = SecurePage(context.browser)

def after_scenario(context, scenario):
    context.browser.quit()