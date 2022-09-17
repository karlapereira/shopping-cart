from os import environ

from motor.motor_asyncio import AsyncIOMotorClient


class DataBase:
    client: AsyncIOMotorClient = None
    database_uri = environ.get("DATABASE_URI")
    users_collection = None
    address_collection = None
    product_collection = None
    order_collection = None
    order_collection = None

db = DataBase()

async def connect_db():
    db.client = AsyncIOMotorClient(
        db.database_uri,
        maxPoolSize=10,
        minPoolSize=10,
        tls=True,
        tlsAllowInvalidCertificates=True
    )
    db.users_collection = db.client.shopping_cart.user
    db.address_collection = db.client.shopping_cart.address
    db.product_collection = db.client.shopping_cart.product
    db.order_collection = db.client.shopping_cart.order
    db.order_collection = db.client.shopping_cart.order_item

async def disconnect_db():
    db.client.close()
