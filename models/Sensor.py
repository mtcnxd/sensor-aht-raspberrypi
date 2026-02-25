from classes.DataBase import *

class Sensor:
    def __init__(self):
        self.table = "sensors"
        self.database = DataBase()
    
    def find(self, id):
        query = f"SELECT * FROM {self.table} WHERE id = {id}"
        return self.database.select_one(query)

    def get(self, id):
        query = f"SELECT * FROM {self.table} WHERE id = {id}"
        return self.database.select_all(query)

    def first(self, key):
        query = f"SELECT * FROM {self.table} WHERE {key} LIMIT 1"
        return self.database.select_one(query)
    
    def last(self):
        query = f"SELECT * FROM {self.table} ORDER BY ID DESC LIMIT 1"
        return self.database.select_one(query)

    def create(self, data):
        columns = ",".join(data.keys())
        placeholders = ",".join(["%s"] * len(data))
        values = tuple(data.values())

        query = f"INSERT INTO {self.table} ({columns}) VALUES ({placeholders})"

        return self.database.query(query, values)

    def update(self, id, data):
        columns = ",".join(data.keys())
        placeholders = ",".join(["%s"] * len(data))
        values = tuple(data.values())

        query = f"UPDATE {self.table} SET {columns} = {placeholders} WHERE id = {id}"

        return self.database.query(query, values)

    # Custom query for load AVG

    def ema_daily(self):
        query = f"SELECT AVG(location) as avg FROM {self.table} WHERE created_at > NOW() - INTERVAL 1 DAY LIMIT 1"
        return self.database.select_one(query)