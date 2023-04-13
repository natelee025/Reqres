# UI
import pytest
from schemas.resources_schemas import *
from data.locators.locators import Resources as res
from data.locators.locators import CommonLocators as cl
from data.status_code import *

list_resource = [Success.OK, ResourcesList]


@pytest.mark.ui
@pytest.mark.parametrize('status_code, schema', (list_resource,), ids=['list_resource ', ])
def test_list_resource(res_ui, status_code, schema):
    res_ui.click_on(res.GET_RESOURCE)
    res_ui.click_on(cl.TRY_IT_OUT_BTN)
    res_ui.click_on(cl.EXECUTE_BTN)
    res_ui.assert_res_status_code(status_code)
    res_ui.validate_res_schema(schema)


single_resource = [Success.OK, SingleResource]


@pytest.mark.ui
@pytest.mark.parametrize('status_code, schema', (single_resource,), ids=['single_resource ', ])
def test_single_resource(res_ui, status_code, schema):
    res_ui.click_on(res.GET_RESOURCE_ID)
    res_ui.click_on(cl.TRY_IT_OUT_BTN)
    res_ui.res_enter_id(2)
    res_ui.click_on(cl.EXECUTE_BTN)
    res_ui.assert_res_status_code(status_code)
    res_ui.validate_res_schema(schema)


single_resource_not_found = [22, Errors.NOT_FOUND, EmptySchema]


@pytest.mark.ui
@pytest.mark.parametrize('user_id, status_code, schema', (single_resource_not_found,),
                         ids=['single_resource_not_found ', ])
def test_single_resource_not_found(res_ui, user_id, status_code, schema):
    res_ui.click_on(res.GET_RESOURCE_ID)
    res_ui.click_on(cl.TRY_IT_OUT_BTN)
    res_ui.res_enter_id(user_id)
    res_ui.click_on(cl.EXECUTE_BTN)
    res_ui.assert_res_status_code(status_code)
    res_ui.validate_res_schema(schema)
