import os
import psycopg2 as psql
from dotenv import load_dotenv
load_dotenv()

class Database:
    @staticmethod
    async def connect(query, query_type):
        db = psql.connect(
            database = os.getenv("db_name"),
            user = os.getenv("db_user"),
            password = os.getenv("db_password"),
            host = os.getenv("db_host"),
            port = os.getenv("db_port")
        )
        cursor = db.cursor()
        data = ["insert", "delete"]
        cursor.execute(query)
        if query_type in data:
            db.commit()
            if query_type == "insert":
                return "inserted successfully"
        else:
            return cursor.fetchall()

    @staticmethod
    async def check_user_id(tg_id: int, full_data_new_user):
        query = f"SELECT full_name, user_name, tg_id FROM bot_users WHERE tg_id = {tg_id}"
        check_user = await Database.connect(query, query_type="select")
        if len(check_user) == 1:
            print("Qayta start bosdi: ", check_user)
            return True
        print("Birinchi marta start bosdi: ", full_data_new_user)
        return False
