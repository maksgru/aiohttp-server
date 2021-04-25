from aiopg.sa import create_engine
from sqlalchemy import MetaData

convention = {
  "ix": 'ix_%(column_0_label)s',
  "uq": "uq_%(table_name)s_%(column_0_name)s",
  "ck": "ck_%(table_name)s_%(constraint_name)s",
  "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
  "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

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