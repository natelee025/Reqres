import pytest
from pageclasses.users import UsersAPI, UsersUI
from pageclasses.resources import ResourcesUI
from pageclasses.register import RegisterUI
from pageclasses.login import LoginUI

import requests
from data.json_requests import *
import config
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def create_user():
    users_endpoint = config.BASE_URL + config.USERS_ENDPOINT
    response = requests.post(url=users_endpoint, data=UsersReq.create_user)
    return response


@pytest.fixture()
def user_exists(create_user):
    return UsersAPI(create_user)


@pytest.fixture()
def get_chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--headless')
    #отключаем sanbox, который используетс для безопасности, т.к. он может мешать автотестам
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-gpu')
    return options


@pytest.fixture()
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    return driver


@pytest.fixture()
def setup(get_webdriver):
    driver = get_webdriver
    url = config.BASE_URL_UI
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture()
def users_ui(setup):
    return UsersUI(setup)


@pytest.fixture()
def res_ui(setup):
    return ResourcesUI(setup)


@pytest.fixture()
def reg_ui(setup):
    return RegisterUI(setup)


@pytest.fixture()
def login_ui(setup):
    return LoginUI(setup)
