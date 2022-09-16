from os import environ

from motor.motor_asyncio import AsyncIOMotorClient


class DbSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        database = environ.get("DATABASE_URI")
        if database not in cls._instances:
            cls._instances[database] = super(DbSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[database]


class Database(metaclass=DbSingleton):
    def __init__(self,
        database_uri=environ.get("DATABASE_URI")
    ) -> None:
        self.client: AsyncIOMotorClient = None
        self.database_uri = database_uri
        self.db = None

    async def connect_db(self):
        self.client = AsyncIOMotorClient(
            self.database_uri,
            maxPoolSize=10,
            minPoolSize=10
        )
        self.db = self.client.shopping_cart

    async def disconnect_db(self):
        self.client.close()
