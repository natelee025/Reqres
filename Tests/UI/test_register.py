# UI
import pytest
from schemas.register_schema import *
from data.locators.locators import Register as reg
from data.locators.locators import CommonLocators as cl
from data.status_code import *
from data.json_requests import *

successful_register = [RegisterUser.register_user, Success.OK, RegisterSchema]


@pytest.mark.ui
@pytest.mark.parametrize('data, status_code, schema', (successful_register,), ids=['successful_register', ])
def test_successful_register(reg_ui, data, status_code, schema):
    reg_ui.click_on(reg.POST_REGISTER)
    reg_ui.click_on(cl.TRY_IT_OUT_BTN)
    reg_ui.reg_enter_request_body(data)
    reg_ui.click_on(cl.EXECUTE_BTN)
    reg_ui.assert_reg_status_code(status_code)
    reg_ui.validate_reg_schema(schema)


unsuccessful_register = [RegisterUser.fail_register_user, Errors.BAD_REQUEST, RegisterErrorSchema]


@pytest.mark.ui
@pytest.mark.parametrize('data, status_code, schema', (unsuccessful_register,), ids=['unsuccessful_register', ])
def test_unsuccessful_register(reg_ui, data, status_code, schema):
    reg_ui.click_on(reg.POST_REGISTER)
    reg_ui.click_on(cl.TRY_IT_OUT_BTN)
    reg_ui.reg_enter_request_body(data)
    reg_ui.click_on(cl.EXECUTE_BTN)
    reg_ui.assert_reg_status_code(status_code)
    reg_ui.validate_reg_schema(schema)
