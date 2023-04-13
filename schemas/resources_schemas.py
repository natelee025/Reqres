from pydantic import BaseModel, StrictStr, StrictInt


class Data(BaseModel):
    id: StrictInt
    name: StrictStr
    year: StrictInt
    color: StrictStr
    pantone_value: StrictStr


class Support(BaseModel):
    url: StrictStr
    text: StrictStr


class ResourcesList(BaseModel):
    page: StrictInt
    per_page: StrictInt
    total: StrictInt
    total_pages: StrictInt
    data: list[Data]
    support: Support


class SingleResource(BaseModel):
    data: Data
    support: Support


class EmptySchema(BaseModel):
    pass
