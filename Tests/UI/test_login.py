# UI
import pytest
from schemas.login_schema import *
from data.locators.locators import Login as lg
from data.locators.locators import CommonLocators as cl
from data.status_code import *
from data.json_requests import *

successful_login = [LoginUser.login_user, Success.OK, LoginSchema]


@pytest.mark.smoke
@pytest.mark.ui
@pytest.mark.parametrize('data, status_code, schema', (successful_login,), ids=['successful_login', ])
def test_successful_login(login_ui, data, status_code, schema):
    login_ui.click_on(lg.POST_LOGIN)
    login_ui.click_on(cl.TRY_IT_OUT_BTN)
    login_ui.log_enter_request_body(data)
    login_ui.click_on(cl.EXECUTE_BTN)
    login_ui.assert_log_status_code(status_code)
    login_ui.validate_log_schema(schema)


unsuccessful_login = [LoginUser.fail_login_user, Errors.BAD_REQUEST, LoginErrorSchema]


@pytest.mark.ui
@pytest.mark.parametrize('data, status_code, schema', (unsuccessful_login,), ids=['unsuccessful_login', ])
def test_unsuccessful_login(login_ui, data, status_code, schema):
    login_ui.click_on(lg.POST_LOGIN)
    login_ui.click_on(cl.TRY_IT_OUT_BTN)
    login_ui.log_enter_request_body(data)
    login_ui.click_on(cl.EXECUTE_BTN)
    login_ui.assert_log_status_code(status_code)
    login_ui.validate_log_schema(schema)
