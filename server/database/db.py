from aiopg.sa import create_engine

async def init_pg(app):
    config = app['config']['postgres']
    engine = await create_engine(
        database=config['database'],
        user=config['user'],
        password=config['password'],
        host=config['host'],
        port=config['port'],
        minsize=config['minsize'],
        maxsize=config['maxsize']
    )
    app['db'] = engine

async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()