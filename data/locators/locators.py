from selenium.webdriver.common.by import By


class Users:
    GET_USERS = (By.XPATH, "(//div[@class='opblock-summary opblock-summary-get'])[2]")
    GET_USERS_ID = (By.XPATH, "(//div[@class='opblock-summary opblock-summary-get'])[3]")
    PUT_UPD_USER = (By.XPATH, "(//div[@class='opblock-summary opblock-summary-put'])[1]")
    PATCH_UPD_USER = (By.XPATH, "(//div[@class='opblock-summary opblock-summary-patch'])[1]")
    DELETE_USER = (By.XPATH, "(//div[@class='opblock-summary opblock-summary-delete'])[1]")


class Resources:
    GET_RESOURCE = (By.XPATH, "(//div[@class='opblock-summary opblock-summary-get'])[1]")
    GET_RESOURCE_ID = (By.XPATH, "(//div[@class='opblock-summary opblock-summary-get'])[4]")
    PUT_RESOURCE_ID = (By.XPATH, "(//div[@class='opblock-summary opblock-summary-put'])[2]")
    PATCH_RESOURCE_ID = (By.XPATH, "(//div[@class='opblock-summary opblock-summary-patch'])[2]")
    DELETE_RESOURCE_ID = (By.XPATH, "(//div[@class='opblock-summary opblock-summary-delete'])[2]")


class Register:
    POST_REGISTER = (By.XPATH, "(//div[@class='opblock-summary opblock-summary-post'])[2]")


class Login:
    POST_LOGIN = (By.XPATH, "(//div[@class='opblock-summary opblock-summary-post'])[1]")
    POST_LOGOUT = (By.XPATH, "(//div[@class='opblock-summary opblock-summary-post'])[3]")


class CommonLocators:
    TRY_IT_OUT_BTN = (By.CSS_SELECTOR, '.btn.try-out__btn')
    EXECUTE_BTN = (By.CSS_SELECTOR, '.btn.execute.opblock-control__btn')
    PAGE_FIELD = (By.XPATH, "//*[@placeholder='page']")
    PER_PAGE_FIELD = (By.XPATH, "//*[@placeholder='per_page']")
    ID_FIELD = (By.XPATH, "//*[@placeholder='id']")
    RESPONSE_JSON = (By.XPATH, "(//code[@class='language-json'])[1]")
    RESPONSE_STATUS_CODE = (By.CSS_SELECTOR, '.responses-table.live-responses-table .response .response-col_status')
    REQUEST_BODY = (By.CSS_SELECTOR, '.body-param__text')
    # REQUEST_BODY = (By.XPATH, "//div[@class='body-param']")
    RESPONSE_ERROR_STATUS_CODE = (By.XPATH, "(//*[starts-with(text(), 'Error: response status is')])")
