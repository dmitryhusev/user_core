import re
from playwright.sync_api import Page, expect
from faker import Faker

url = "http:localhost:8000/accounts/signup"

def test_has_title(page: Page):
    page.goto(url)

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Sign up"))

def test_get_started_link(page: Page):
    fake = Faker()
    password = fake.password()
    page.goto(url)
    page.get_by_label('Email').fill(fake.email())
    page.locator('//*[@name="password1"]').fill(password)
    page.locator('//*[@name="password2"]').fill(password)
    page.get_by_text('Sign up').click()
    expect(page).to_have_title(re.compile("Log in"))

