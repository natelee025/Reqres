from pydantic import BaseModel, StrictStr


class LoginSchema(BaseModel):
    token: StrictStr


class LoginErrorSchema(BaseModel):
    error: StrictStr
