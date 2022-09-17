import asyncio

from src.controllers.users import users_crud
# from src.controllers.products import products_crud
# from src.controllers.carrinho import carrinho_crud

loop = asyncio.get_event_loop()
loop.run_until_complete(users_crud())
