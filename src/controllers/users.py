from src.models.user import (
    create_user,
    get_user_by_email,
    update_user,
    delete_user,
    get_users
)
from src.server.database import connect_db, db, disconnect_db


async def users_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    users_collection = db.users_collection

    user =  {
        "email": "lu_domagalu@gmail.com",
        "password": "213sd312re3",
        "is_active": True,
        "is_admin": False
    }

    if option == '1':
        # create user
        user = await create_user(
            users_collection,
            user
        )
        print(user)
    elif option == '2':
        # get user
        user = await get_user_by_email(
            users_collection,
            user["email"]
        )
        print(user)
    elif option == '3':
        # update
        user = await get_user_by_email(
            users_collection,
            user["email"]
        )

        user_data = {
            "password": 'new_password1234'
        }

        is_updated, numbers_updated = await update_user(
            users_collection,
            user["_id"],
            user_data
        )
        if is_updated:
            print(f"Atualização realizada com sucesso, número de documentos alterados {numbers_updated}")
        else:
            print("Atualização falhou!")
    elif option == '4':
        # delete
        user = await get_user_by_email(
            users_collection,
            user["email"]
        )

        result = await delete_user(
            users_collection,
            user["_id"]
        )

        print(result)

    elif option == '5':
        # pagination
        users = await get_users(
            users_collection,
            skip=2,
            limit=2
        )
        print(users)

    await disconnect_db()
