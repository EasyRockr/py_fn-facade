import sqlite3
import os

class DbDaoABC:
    def _get_db_connection(self):
        base_dir = os.path.dirname(__file__)
        db_path = os.path.join(base_dir, "..", "address_book1.db")
        db_path = os.path.abspath(db_path)
        return sqlite3.connect(db_path)

    def execute_select(self, sql, params=None):
        with self._get_db_connection() as cnn:
            cursor = cnn.cursor()
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            return cursor.fetchall()
