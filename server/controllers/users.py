from server.services import user
from aiohttp import web

async def get_one_user(request: web.Request):
    try:
        db = request.app['db'].acquire
        user_id = request.match_info.get('id')
        user_data = await user.get_user(db, user_id)
        return web.json_response(user_data)
    except Exception as exc:
        return web.json_response({ 'message': exc.args })

async def get_users(request: web.Request):
    try:
        db = request.app['db'].acquire
        users_list = await user.get_users(db)
        return web.json_response(users_list)
    except Exception as exc:
        return web.json_response({'message': exc.args})

async def create_user(request: web.Request):
    try:
        db = request.app['db'].acquire
        data = await request.json()
        new_user = await user.create_user(db, data)
        return web.json_response(new_user)
    except Exception as exc:
        return web.json_response({'message': exc.args})