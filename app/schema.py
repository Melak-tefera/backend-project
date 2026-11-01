from pydantic import BaseModel, ConfigDict
class Usercreate(BaseModel):
    name: str
class Userread(BaseModel):
    id: int
    name: str
model_config = ConfigDict(from_attributes=True)
