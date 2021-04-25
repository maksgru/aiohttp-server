from sqlalchemy import create_engine, MetaData
from server.db.models.user import user
from config import config

DSN = 'postgresql://{user}:{password}@{host}:{port}/{database}'

def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[user])

if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    engine = create_engine(db_url)
    create_tables(engine)
