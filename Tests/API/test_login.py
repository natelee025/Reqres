# API
import allure
import requests
from pageclasses.login import LoginAPI
import config
import pytest
from data.status_code import *
from schemas.login_schema import *
from data.json_requests import *

# url+endpoint for login
log_endpoint = config.BASE_URL + config.LOGIN_ENDPOINT

successful_login = [LoginUser.login_user, Success.OK, LoginSchema]

@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.parametrize('data, status_code, schema', (successful_login,), ids=['successful_login', ])
def test_successful_login(data, status_code, schema):
    with allure.step("Отправляем запрос на авторизацию"):
        response = requests.post(url=log_endpoint, data=data, headers={'User-Agent': 'PostmanRuntime/7.36.1', 'Accept': '*/*'})
    log = LoginAPI(response)
    log.assert_status_code(status_code)
    log.val_login_schema(schema)
    log.assert_login_headers()


unsuccessful_login = [LoginUser.fail_login_user, Errors.BAD_REQUEST, LoginErrorSchema]


@pytest.mark.api
@pytest.mark.parametrize('data, status_code, schema', (unsuccessful_login,), ids=['unsuccessful_login: only email', ])
def test_unsuccessful_login(data, status_code, schema):
    response = requests.post(url=log_endpoint, data=data)
    log = LoginAPI(response)
    log.assert_status_code(status_code)
    log.val_login_schema(schema)
    log.assert_login_headers()
