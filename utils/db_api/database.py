import asyncpg

from data.config import POSTGRES

conn: asyncpg.connection.Connection = None


async def create_conn():
    global conn
    conn = await asyncpg.connect(POSTGRES['host'], password=POSTGRES['password'])


class UsersDb:
    @staticmethod
    async def user_exists(user_id):
        query = f"select * from users where user_id = {user_id}"
        return conn.fetchval(query)

    @staticmethod
    async def register_user(user_id):
        query = f"insert into users(user_id) values ({user_id})"
        await conn.execute(query)