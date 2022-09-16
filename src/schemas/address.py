from typing import List
from pydantic import BaseModel, Field

from src.schemas.user import UserSchema


class Address(BaseModel):
    street: str
    cep: str
    district: str
    city: str
    state: str
    is_delivery: bool = Field(default=True)


class AddressSchema(BaseModel):
    user: UserSchema
    address: List[Address] = []
