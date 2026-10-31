import string
import pytest
from faker import Faker
from selenium import webdriver


url = "https://qa-desk.education-services.ru/"
faker = Faker()


@pytest.fixture(scope='function')
def driver():

    browser = webdriver.Chrome()
    browser.get(url)
    
    yield browser
    browser.quit()
    
@pytest.fixture()
def email():
    letters = string.ascii_lowercase
    return faker.lexify("???????@???????.???", letters=letters)

@pytest.fixture
def wrong_email():
    letters = string.ascii_lowercase
    return faker.lexify("?????????", letters=letters)


@pytest.fixture(scope='class')
def existing_email(email):
    return email

@pytest.fixture
def login_existing_email():
    return "zupzdpc@pgxuemg.amm"
