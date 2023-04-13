class Success:
    OK = 200
    CREATED = 201
    NOT_CONTENT = 204


class Errors:
    NOT_FOUND = 404
    BAD_REQUEST = 400


class InDocument:
    UsersInDoc = [Success.OK, Success.NOT_CONTENT]
    ResInDoc = [Success.OK, Success.NOT_CONTENT]
    RegInDoc = [Success.OK, Errors.BAD_REQUEST]
    LogInDoc = [Success.OK, Errors.BAD_REQUEST]



