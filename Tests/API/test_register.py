# API
import requests
from pageclasses.register import RegisterAPI
import config
import pytest
from data.status_code import *
from schemas.register_schema import *
from data.json_requests import *

# url+endpoint for register
reg_endpoint = config.BASE_URL + config.REGISTER_ENDPOINT

successful_register = [RegisterUser.register_user, Success.OK, RegisterSchema]


@pytest.mark.skip("Сломался")
@pytest.mark.api
@pytest.mark.parametrize('data, status_code, schema', (successful_register,), ids=['successful_register', ])
def test_successful_register(data, status_code, schema):
    response = requests.post(url=reg_endpoint, data=data)
    reg = RegisterAPI(response)
    reg.assert_status_code(status_code)
    reg.val_reg_schema(schema)
    reg.assert_reg_headers()


unsuccessful_register = [RegisterUser.fail_register_user, Errors.BAD_REQUEST, RegisterErrorSchema]


@pytest.mark.api
@pytest.mark.parametrize('data, status_code, schema', (unsuccessful_register,),
                         ids=['unsuccessful_register: only email', ])
def test_unsuccessful_register(data, status_code, schema):
    response = requests.post(url=reg_endpoint, data=data)
    reg = RegisterAPI(response)
    reg.assert_status_code(status_code)
    reg.val_reg_schema(schema)
    reg.assert_reg_headers()
