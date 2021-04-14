from aiohttp import web
from server.database.db import init_pg, close_pg
from settings import config 


async def foo(request):
    return web.Response(text="Hello, world")


app = web.Application()
app['config'] = config
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)
app.add_routes([web.get('/', foo)])

web.run_app(app, host='127.0.0.1', port=4000)