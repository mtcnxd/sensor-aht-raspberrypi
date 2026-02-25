import pymysql.cursors
import configs

class DataBase:
    def __init__(self):
        try: 
            self.connection = pymysql.connect(
                host="127.0.0.1",
                user=configs.db_user,
                password=configs.db_pass,
                db="BitsoData",
                charset="utf8mb4",
            )
            self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        
        except Exception as e:
            print("AN ERROR OCURRED WHILE CONNECTING: {e}")

    def __del__(self):
        self.connection.close()

    def select_all(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()

        except Exception as e:
            print(f"AN ERROR OCURRED WHILE EXECUTE QUERY: {e}")
            return None

    def select_one(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchone()

        except Exception as e:
            print(f"AN ERROR OCURRED WHILE EXECUTE QUERY: {e}")
            return None

    def query(self, query, values):
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
        
        except Exception as e:
            print(f"AN ERROR OCURRED WHILE INSERT DATA: {e}")