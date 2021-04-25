from aiohttp import web
from server.controllers.users import get_users, get_one_user, create_user

def routes(route: web.RouteTableDef):
    return [
        route.get('/', get_users),
        route.get('/{id}', get_one_user),
        route.post('/', create_user)
    ]