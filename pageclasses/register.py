from baseclasses.base_api import Response
from baseclasses.base_ui import BasePage
from data.locators.locators import CommonLocators as cl
from data.status_code import InDocument as in_doc


class RegisterAPI(Response):
    def val_reg_schema(self, schema):
        self.validate_schema(schema)

    def assert_reg_headers(self):
        headers = ['Connection', 'Content-Type']
        expected_values = ['keep-alive', 'application/json; charset=utf-8']
        self.assert_some_headers(headers, expected_values)


class RegisterUI(BasePage):
    def reg_enter_page(self, user_id):
        self.to_send_keys(cl.ID_FIELD, user_id)

    # def assert_reg_status_code(self, status_code):
    #     self.assert_status_code(locator=cl.RESPONSE_STATUS_CODE, status_in_doc=str(status_code),
    #                             status_not_in_doc=str(status_code) + '\nUndocumented')

    def assert_reg_status_code(self, status_code):
        self.assert_status_code(locator=cl.RESPONSE_STATUS_CODE, in_doc=in_doc.RegInDoc, expected_text=status_code)

    def validate_reg_schema(self, schema):
        self.validate_schema(schema=schema, locator=cl.RESPONSE_JSON)

    def reg_enter_request_body(self, body):
        self.enter_body(cl.REQUEST_BODY, body)
