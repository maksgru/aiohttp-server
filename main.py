from server.controllers import set_routes
from aiohttp import web
import aiohttp_debugtoolbar
import logging
from server.database.db import init_pg, close_pg
from config import config
from server.routes import web_routes

routes = web_routes(web)
app = web.Application()
aiohttp_debugtoolbar.setup(app)
app['config'] = config
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)
app.add_routes(routes)

logging.basicConfig(level=logging.DEBUG)
web.run_app(app, host='127.0.0.1', port=4000)