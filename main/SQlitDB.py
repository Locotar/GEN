import sqlite3


class connect_db:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('db.sqlite3')
        except:
            pass

    def selectfromtable(self , table , key = '*'):
        try:
            cursor = self.conn.execute("SELECT " + key + " from " + table)
            return cursor
        except:
            return None

    def deletefromtable(self, table, keyid = None):
        try:
            cursor = self.conn.execute("DELETE FROM " + table + " WHERE ID=" + keyid )
            return cursor
        except:
            return None
