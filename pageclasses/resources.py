from baseclasses.base_api import Response
from baseclasses.base_ui import BasePage
from data.locators.locators import CommonLocators as cl
from data.status_code import InDocument as in_doc


class ResourcesAPI(Response):
    def val_resources_schema(self, schema):
        self.validate_schema(schema)

    def assert_resources_headers(self):
        headers = ['Connection', 'Content-Type']
        expected_values = ['keep-alive', 'application/json; charset=utf-8']
        self.assert_some_headers(headers, expected_values)

    def assert_res_elements_values(self, value):
        self.assert_element_value("data/id", value)


class ResourcesUI(BasePage):
    def res_enter_page(self, user_id):
        self.to_send_keys(cl.ID_FIELD, user_id)

    def assert_res_status_code(self, status_code):
        self.assert_status_code(locator=cl.RESPONSE_STATUS_CODE, in_doc=in_doc.ResInDoc, expected_text=status_code)

    def validate_res_schema(self, schema):
        self.validate_schema(schema=schema, locator=cl.RESPONSE_JSON)

    def res_not_have_response_body(self):
        self.is_not_visible(cl.RESPONSE_JSON)

    def res_enter_request_body(self, body):
        self.to_send_keys(cl.REQUEST_BODY, body)

    def res_enter_id(self, user_id):
        self.to_send_keys(cl.ID_FIELD, user_id)
