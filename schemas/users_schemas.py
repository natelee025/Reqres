from pydantic import BaseModel, StrictStr, StrictInt
from typing import Optional


class Data(BaseModel):
    id: StrictInt
    email: StrictStr
    first_name: StrictStr
    last_name: StrictStr
    avatar: StrictStr


class Support(BaseModel):
    url: StrictStr
    text: StrictStr


class UsersList(BaseModel):
    page: StrictInt
    per_page: StrictInt
    total: StrictInt
    total_pages: StrictInt
    data: list[Data]
    support: Support


class SingleUser(BaseModel):
    data: Data
    support: Support


class EmptySchema(BaseModel):
    pass


class CreateUser(BaseModel):
    name: StrictStr
    job: StrictStr
    id: StrictStr
    createdAt: StrictStr


class UpdateUser(BaseModel):
    name: Optional[StrictStr] = None
    job: Optional[StrictStr] = None
    updatedAt: StrictStr
