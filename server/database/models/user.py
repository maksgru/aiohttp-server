from sqlalchemy import (
    MetaData, Table, Column
)
from sqlalchemy.sql.sqltypes import Integer, String

meta = MetaData()

user = Table(
    'user', meta,
    Column('id', Integer, primary_key=True),
    Column('email', String, nullable=False)
)
