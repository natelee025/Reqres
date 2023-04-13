# API
import requests
from pageclasses.resources import ResourcesAPI
import config
import pytest
from data.status_code import *
from schemas.resources_schemas import *

# url+endpoint for resources
res_endpoint = config.BASE_URL

list_unknown_res = ['unknown', Success.OK, ResourcesList]


@pytest.mark.parametrize('resource, status_code, schema', (list_unknown_res,), ids=['list_unknown_resource', ])
def test_list_resource(resource, status_code, schema):
    response = requests.get(url=res_endpoint + f'/{resource}')
    res = ResourcesAPI(response)
    res.assert_status_code(status_code)
    res.validate_schema(schema)
    res.assert_resources_headers()


single_unknown_res = ['unknown', 2, Success.OK, SingleResource]


@pytest.mark.api
@pytest.mark.parametrize('resource, user_id, status_code, schema', (single_unknown_res,),
                         ids=['single_unknown_resource', ])
def test_single_resource(resource, user_id, status_code, schema):
    response = requests.get(url=res_endpoint + f'/{resource}' + f'/{user_id}')
    res = ResourcesAPI(response)
    res.assert_status_code(status_code)
    res.val_resources_schema(schema)
    res.assert_resources_headers()
    res.assert_res_elements_values(user_id)


non_existent_resource = ['unknown', 23, Errors.NOT_FOUND, EmptySchema]
zero_resource = ['unknown', 0, Errors.NOT_FOUND, EmptySchema]


@pytest.mark.api
@pytest.mark.parametrize('resource, user_id, status_code, schema', (non_existent_resource, zero_resource),
                         ids=['non_existent_resource', 'zero_resource'])
def test_single_resource_not_found(resource, user_id, status_code, schema):
    response = requests.get(url=res_endpoint + f'/{resource}' + f'/{user_id}')
    res = ResourcesAPI(response)
    res.assert_status_code(status_code)
    res.val_resources_schema(schema)
