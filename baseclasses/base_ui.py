import json
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def is_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def is_not_visible(self, locator):
        return self.wait.until(ec.invisibility_of_element_located(locator))

    def to_send_keys(self, locator, key):
        self.is_visible(locator).send_keys(key)

    def are_visible(self, locator):
        return self.wait.until(ec.visibility_of_all_elements_located(locator))

    def is_clickable(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))

    def click_on(self, *locator):
        for i in locator:
            self.is_clickable(i).click()

    def clear_field(self, locator):
        self.is_visible(locator).clear()

    def get_text(self, locator):
        return self.is_visible(locator).text

    def assert_text(self, locator, expected_text):
        actual_text = self.get_text(locator)
        assert expected_text == actual_text, f'Failed. We expected text: {expected_text}, but got {actual_text}'

    def get_statuses_in_doc(self, in_doc):
        list_indoc = []
        for i in in_doc:
            status = str(i)
            list_indoc.append(status)
        return list_indoc

    def assert_status_code(self, locator, in_doc, expected_text):
        actual_text = self.get_text(locator)
        list_statuses = self.get_statuses_in_doc(in_doc)
        if actual_text in list_statuses:
            assert str(expected_text) == str(actual_text), \
                f'Failed. We expected status code: {expected_text}, but got {actual_text}'
        else:
            not_indoc_text = str(expected_text) + '\nUndocumented'
            assert str(
                actual_text) == not_indoc_text, f'Failed. We expected undocument status code: {expected_text}, but got {actual_text}'

    # def assert_status_code(self, locator, status_in_doc):
    #     actual_text = self.get_text(locator)
    #     assert status_in_doc == actual_text, f'Failed. We got wrong/unexpected {actual_text}'

    def validate_schema(self, schema, locator):
        schema_text = self.get_text(locator)
        schema_dict = eval(schema_text)
        schema.parse_obj(schema_dict)

    def enter_body(self, locator, body):
        self.click_on(locator)
        self.clear_field(locator)
        body_json = json.dumps(body)
        self.to_send_keys(locator, body_json)
