# API
import requests
from pageclasses.users import UsersAPI
import config
import pytest
from data.status_code import *
from data.json_requests import *
from schemas.users_schemas import *

# url+endpoint for users
users_endpoint = config.BASE_URL + config.USERS_ENDPOINT

with_page_param = ['page=2', Success.OK, UsersList, 6, [2, 6, 12, 2]]


@pytest.mark.parametrize('params, status_code, schema, users_number, elements_values, ', (with_page_param,),
                         ids=['with page parameter', ])
def test_get_users_list(params, status_code, schema, users_number, elements_values):
    response = requests.get(url=users_endpoint, params=params)
    users = UsersAPI(response)
    users.assert_status_code(status_code)
    users.val_users_schema(UsersList)
    users.assert_users_headers()
    users.count_users_number(users_number)
    users.assert_users_list_elements_values(elements_values)


first_user = [1, Success.OK, SingleUser]
last_user = [12, Success.OK, SingleUser]


@pytest.mark.parametrize('user_id, status_code, schema', (first_user, last_user),
                         ids=['get first user by id', 'get last user by id'])
def test_get_single_user(user_id, status_code, schema):
    response = requests.get(url=users_endpoint + f'/{user_id}')
    users = UsersAPI(response)
    users.assert_status_code(status_code)
    users.val_users_schema(schema)
    users.assert_users_headers()
    users.assert_user_elements_values(user_id)


non_existent_user = [23, Errors.NOT_FOUND, EmptySchema]
zero_user = [0, Errors.NOT_FOUND, EmptySchema]


@pytest.mark.parametrize('user_id, status_code, schema', (non_existent_user, zero_user),
                         ids=['not found non-existent user by id', 'not found zero user by id'])
def test_single_user_not_found(user_id, status_code, schema):
    response = requests.get(url=users_endpoint + f'/{user_id}')
    users = UsersAPI(response)
    users.assert_status_code(status_code)
    users.val_users_schema(schema)
    users.assert_users_headers()


create_user = [Success.CREATED, CreateUser, UsersReq.create_user,
               [UsersReq.create_user['name'], UsersReq.create_user['job']]]


@pytest.mark.parametrize('status_code, schema, data, info', (create_user,), ids=['create_user', ])
def test_create_user(status_code, schema, data, info):
    response = requests.post(url=users_endpoint, data=data)
    users = UsersAPI(response)
    users.assert_status_code(status_code)
    users.val_users_schema(schema)
    users.assert_users_headers()
    users.assert_user_info(info)
    users.assert_user_created_at_datetime()


full_update_user = [Success.OK, UpdateUser, UsersReq.full_upd_user,
                    [UsersReq.full_upd_user['name'], UsersReq.full_upd_user['job']]]


@pytest.mark.parametrize('status_code, schema, data, info', (full_update_user,), ids=['full_update_user', ])
def test_full_update_user(user_exists, status_code, schema, data, info):
    user_id = user_exists.get_id()
    response = requests.put(url=users_endpoint + f'/{user_id}', data=data)
    users = UsersAPI(response)
    users.assert_status_code(status_code)
    users.val_users_schema(schema)
    users.assert_users_headers()
    users.assert_user_info(info)
    users.assert_user_updated_at_datetime()


part_update_user = [Success.OK, UpdateUser, UsersReq.part_upd_user,
                    [UsersReq.part_upd_user['name'], UsersReq.part_upd_user['job']]]


@pytest.mark.parametrize('status_code, schema, data, info', (part_update_user,), ids=['part_update_user', ])
def test_part_update_user(user_exists, status_code, schema, data, info):
    user_id = user_exists.get_id()
    response = requests.patch(url=users_endpoint + f'/{user_id}', data=data)
    users = UsersAPI(response)
    users.assert_status_code(status_code)
    users.val_users_schema(schema)
    users.assert_users_headers()
    users.assert_user_info(info)
    users.assert_user_updated_at_datetime()


delete_user = [2, 204]


@pytest.mark.api
@pytest.mark.parametrize('user_id, status_code', (delete_user,), ids=['delete_user', ])
def test_delete_user(user_id, status_code):
    response = requests.delete(url=users_endpoint + f'/{user_id}')
    users = UsersAPI(response)
    users.assert_status_code(status_code)


delayed_response = [3, Success.OK, UsersList, 3.999999]


@pytest.mark.api
@pytest.mark.parametrize('delay, status_code, schema, border', (delayed_response,), ids=['delayed_response', ])
def test_delayed_response(delay, status_code, schema, border):
    response = requests.get(url=users_endpoint, params=f'delay={delay}')
    users = UsersAPI(response)
    users.assert_status_code(status_code)
    users.assert_response_time(border)
    users.val_users_schema(schema)
