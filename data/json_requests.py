class UsersReq:
    create_user = {
        "name": "morpheus",
        "job": "leader"
    }
    full_upd_user = {
        "name": "noname_1",
        "job": "hero"
    }
    part_upd_user = {
        "name": "noname_2",
        "job": "hero"
    }


class RegisterUser:
    register_user = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    fail_register_user = {
        "email": "eve.holt@reqres.in"
    }


class LoginUser:
    login_user = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    fail_login_user = {
        "email": "eve.holt@reqres.in"
    }
