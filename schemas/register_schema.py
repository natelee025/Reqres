from pydantic import BaseModel, StrictInt, StrictStr


class RegisterSchema(BaseModel):
    id: str
    token: StrictStr


class RegisterErrorSchema(BaseModel):
    error: StrictStr
