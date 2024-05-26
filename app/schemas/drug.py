from pydantic import BaseModel

class CommonDto(BaseModel):
    value: int
    label: str

