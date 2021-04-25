from sqlalchemy import (
    Table, Column
)
from sqlalchemy.sql.sqltypes import Integer, String
from server.db import metadata

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String, nullable=False),
    Column('password', String, nullable=False)
)
