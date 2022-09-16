from pydantic import BaseModel

from src.schemas.order import OrderSchema
from src.schemas.product import ProductSchema


class OrderItemSchema(BaseModel):
    order: OrderSchema
    product: ProductSchema
