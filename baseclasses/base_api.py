import dpath as dp
from datetime import datetime, timezone



class Response:
    def __init__(self, response):
        self.response = response
        self.response_status = response.status_code

    def validate_schema(self, schema):
        schema.model_validate(self.response.json())

    def assert_header(self, header, expected_value):
        actual_value = self.response.headers[header]
        assert actual_value == expected_value, f'Fail. We expected {expected_value}, but got {actual_value}'

    def get_headers_value(self, headers):
        l_headers_values = []
        for i in headers:
            values = self.response.headers[i]
            l_headers_values.append(values)
        return l_headers_values

    def assert_some_headers(self, headers, expected_values):
        if isinstance(headers, list):
            actual_values = self.get_headers_value(headers)
            assert actual_values == expected_values, f'Fail. We expected {expected_values}, but got {actual_values}'
        else:
            self.assert_header(headers, expected_values)

    def assert_status_code(self, expected_code):
        actual_code = self.response_status
        assert actual_code == expected_code, f'Fail. Status code is {actual_code}'

    def get_element_value(self, element):
        actual_value = dp.get(self.response.json(), element)
        return actual_value

    def assert_element_value(self, element, expected_value):
        actual_value = self.get_element_value(element)
        assert actual_value == expected_value, f'Fail. We expected {element} = {expected_value}, but got {actual_value}'

    def assert_datetime_in_response(self, time):
        datetime_response = dp.get(self.response.json(), time)
        date_now_utc = datetime.now(timezone.utc)
        date_now = date_now_utc.strftime("%Y-%m-%dT%H:%M")
        assert date_now in datetime_response, f'{date_now} not in {datetime_response}'

    def get_response_time(self):
        return self.response.elapsed.total_seconds()
