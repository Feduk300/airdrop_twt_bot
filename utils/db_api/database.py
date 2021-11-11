import asyncpg

from data.config import POSTGRES, amount

conn: asyncpg.connection.Connection = None


async def create_conn():
    global conn
    conn = await asyncpg.connect(POSTGRES['host'], password=POSTGRES['password'])


class UsersDb:
    @staticmethod
    async def user_exists(user_id):
        query = f"select * from users where user_id = {user_id}"
        return await conn.fetchval(query)

    @staticmethod
    async def register_user(user_id):
        query = f"insert into users(user_id) values ({user_id})"
        try:
            await conn.execute(query)
        except:
            pass

    @staticmethod
    async def numberprocess(number, user_id):
        query = f"update users set number = '{number}' where user_id = {user_id}"
        await conn.execute(query)

    @staticmethod
    async def fullnameprocess(fullname, user_id):
        query = f"update users set full_name = '{fullname}' where user_id = {user_id}"
        await conn.execute(query)

    @staticmethod
    async def name(user_id):
        query = f"SELECT full_name from users where user_id = {user_id}"
        res = await conn.fetchval(query)
        return res

    @staticmethod
    async def number(user_id):
        query = f"SELECT number from users where user_id = {user_id}"
        res = await conn.fetchval(query)
        return res

    @staticmethod
    async def successfull(user_id):
        query = f"update users set balance = balance+{amount}, has_paid=True where user_id = {user_id}"
        await conn.execute(query)

    @staticmethod
    async def users():
        query = f"SELECT user_id, balance, has_paid, number, full_name from users where has_paid = True"
        res = await conn.fetch(query)
        return res

    @staticmethod
    async def allusersbots():
        query = f"SELECT user_id, balance, has_paid, number, full_name from users where user_id = {user_id}"
        res = await conn.fetch(query)
        return res


    @staticmethod
    async def check_pay():
        query = f"SELECT COUNT(*) from users where has_paid = true"
        return await conn.fetchval(query)