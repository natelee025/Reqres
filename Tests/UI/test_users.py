# UI
import pytest
from schemas.users_schemas import *
from data.locators.locators import Users as us
from data.locators.locators import CommonLocators as cl
from data.status_code import *

with_page_param = [2, Success.OK, UsersList]


@pytest.mark.parametrize('page, status_code, schema', (with_page_param,), ids=['with_page_param', ])
def test_get_list_users(users_ui, page, status_code, schema):
    users_ui.click_on(us.GET_USERS)
    users_ui.click_on(cl.TRY_IT_OUT_BTN)
    users_ui.users_enter_page(page)
    users_ui.click_on(cl.EXECUTE_BTN)
    users_ui.assert_users_status_code(status_code)
    users_ui.validate_user_schema(schema)


first_user = [1, Success.OK, SingleUser]
last_user = [12, Success.OK, SingleUser]


@pytest.mark.parametrize('user_id, status_code, schema', (first_user, last_user),
                         ids=['get first user by id', 'get last user by id'])
def test_get_single_user(users_ui, user_id, status_code, schema):
    users_ui.click_on(us.GET_USERS_ID)
    users_ui.click_on(cl.TRY_IT_OUT_BTN)
    users_ui.users_enter_id(user_id)
    users_ui.click_on(cl.EXECUTE_BTN)
    users_ui.assert_users_status_code(status_code)
    users_ui.validate_user_schema(schema)


non_existent_user = [23, Errors.NOT_FOUND, EmptySchema]
zero_user = [0, Errors.NOT_FOUND, EmptySchema]


@pytest.mark.ui
@pytest.mark.parametrize('user_id, status_code, schema', (non_existent_user, zero_user),
                         ids=['not found non-existent user by id', 'not found zero user by id'])
def test_single_user_not_found(users_ui, user_id, status_code, schema):
    users_ui.click_on(us.GET_USERS_ID)
    users_ui.click_on(cl.TRY_IT_OUT_BTN)
    users_ui.users_enter_id(user_id)
    users_ui.click_on(cl.EXECUTE_BTN)
    users_ui.assert_users_status_code(status_code)
    users_ui.validate_user_schema(schema)


def test_create_user():
    pass


# method is not on page


full_update_user = [Success.OK, UpdateUser]


@pytest.mark.ui
@pytest.mark.parametrize('status_code, schema', (full_update_user,), ids=['full_update_user ', ])
def test_full_update_user(users_ui, status_code, schema):
    users_ui.click_on(us.PUT_UPD_USER)
    users_ui.click_on(cl.TRY_IT_OUT_BTN)
    users_ui.click_on(cl.EXECUTE_BTN)
    users_ui.assert_users_status_code(status_code)
    users_ui.validate_user_schema(schema)


art_update_user = [Success.OK, UpdateUser]


@pytest.mark.ui
@pytest.mark.parametrize('status_code, schema', (art_update_user,), ids=['art_update_user ', ])
def test_part_update_user(users_ui, status_code, schema):
    users_ui.click_on(us.PATCH_UPD_USER)
    users_ui.click_on(cl.TRY_IT_OUT_BTN)
    users_ui.click_on(cl.EXECUTE_BTN)
    users_ui.assert_users_status_code(Success.OK)
    users_ui.validate_user_schema(UpdateUser)


@pytest.mark.ui
def test_delete_user(users_ui):
    users_ui.click_on(us.DELETE_USER)
    users_ui.click_on(cl.TRY_IT_OUT_BTN)
    users_ui.click_on(cl.EXECUTE_BTN)
    users_ui.assert_users_status_code(Success.NOT_CONTENT)
    users_ui.users_not_have_response_body()


def test_delayed_response():
    pass
# method is not on page
