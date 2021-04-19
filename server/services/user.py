from sqlalchemy.sql.elements import literal_column
from server.database.models.user import user


async def create_user(db, data):
    async with db() as conn:
        created = await conn.execute(user.insert()
            .returning(literal_column('*'))
            .values(email=data['email']))
            
        new_user = await created.fetchone()
        return dict(new_user)


async def get_users(db):
    async with db() as conn:
        users_list = await conn.execute(user.select())
        records = await users_list.fetchall()
        return [dict(q) for q in records]


async def get_user(db, user_id):
    async with db() as conn:
        user_data = await conn.execute(user.select().where(user.c.id == user_id))
        one_user = await user_data.fetchone()
        return dict(one_user)
