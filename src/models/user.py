from src.schemas.user import UserSchema
from src.server.database import Database
from src.utils import Hash


class Users:
    def __init__(self, database: Database) -> None:
        self.users_collection = database.users

    async def create_user(self, user: UserSchema):
        try:
            password = Hash.encrypt(user.password)
            user.password = password
            user = await self.users_collection.insert_one(user.dict())

            if user.inserted_id:
                user = await self.get_user(user.inserted_id)
                return user

        except Exception as e:
            print(f'create_user.error: {e}')

    async def get_user(self, user_id):
        try:
            data = await self.users_collection.find_one({'_id': user_id})
            if data:
                return data
        except Exception as e:
            print(f'get_user.error: {e}')

    async def get_users(self, skip, limit):
        try:
            user_cursor = self.users_collection.find().skip(int(skip)).limit(int(limit))
            users = await user_cursor.to_list(length=int(limit))
            return users

        except Exception as e:
            print(f'get_users.error: {e}')

    async def get_user_by_email(self, email):
        user = await self.users_collection.find_one({'email': email})
        return user

    async def update_user(self, user_id, user_data):
        try:
            data = dict(user_data)
            data = {k: v for k, v in data.items() if v is not None}
            user = await self.users_collection.update_one(
                {'_id': user_id}, {'$set': data}
            )

            if user.modified_count:
                return await self.get_user(user)

            return None
        except Exception as e:
            print(f'update_user.error: {e}')

    async def delete_user(self, user_id):
        try:
            user = await self.users_collection.delete_one(
                {'_id': user_id}
            )
            if user.deleted_count:
                return {'status': 'User deleted'}
        except Exception as e:
            print(f'delete_user.error: {e}')
