from src.models.user import Users
from src.server.database import Database


def start():
    database = Database()
    database.connect_db()

    users_collection = Users(database.db)
    users_collection.create_user(
        
    )
