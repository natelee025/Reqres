from baseclasses.base_api import Response
from baseclasses.base_ui import BasePage
from data.locators.locators import CommonLocators as cl
from data.status_code import InDocument as in_doc


class UsersAPI(Response):
    def val_users_schema(self, schema):
        self.validate_schema(schema)

    def assert_users_headers(self):
        headers = ['Connection', 'Content-Type']
        expected_values = ['keep-alive', 'application/json; charset=utf-8']
        self.assert_some_headers(headers, expected_values)

    def count_users_number(self, expected_number):
        actual_users = len(self.response.json()['data'])
        assert actual_users == expected_number, f'Fail. We expected {expected_number} users on page, but got {actual_users}'

    def assert_users_list_elements_values(self, value):
        self.assert_element_value("page", value[0])
        self.assert_element_value("per_page", value[1])
        self.assert_element_value("total", value[2])
        self.assert_element_value("total_pages", value[3])

    def assert_user_elements_values(self, value):
        self.assert_element_value("data/id", value)

    def assert_user_created_at_datetime(self):
        self.assert_datetime_in_response('createdAt')

    def assert_user_updated_at_datetime(self):
        self.assert_datetime_in_response('updatedAt')

    def assert_user_info(self, value):
        self.assert_element_value("name", value[0])
        self.assert_element_value("job", value[1])

    def get_id(self):
        self.get_element_value('id')

    def assert_response_time(self, expected_time):
        actual_time = self.get_response_time()
        assert actual_time <= expected_time, f'Fail. Response time = {actual_time}, ' \
                                             f'we expected no more than {expected_time}'


class UsersUI(BasePage):
    def users_enter_page(self, page):
        self.to_send_keys(cl.PAGE_FIELD, page)

    def users_enter_per_page(self, per_page):
        self.to_send_keys(cl.PER_PAGE_FIELD, per_page)

    def users_enter_id(self, user_id):
        self.to_send_keys(cl.ID_FIELD, user_id)

    def assert_users_status_code(self, status_code):
        self.assert_status_code(locator=cl.RESPONSE_STATUS_CODE, in_doc=in_doc.UsersInDoc, expected_text=status_code)

    def validate_user_schema(self, schema):
        self.validate_schema(schema=schema, locator=cl.RESPONSE_JSON)

    def users_not_have_response_body(self):
        self.is_not_visible(cl.RESPONSE_JSON)
