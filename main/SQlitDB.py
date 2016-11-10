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
            self.conn.commit()
            return cursor
        except:
            return None

    def Addtotable(self, table, value, tableid='id'):
        try:
            self.conn.execute("INSERT INTO " + table + " VALUES ((SELECT max(" + tableid + ") from "
                              + table + ") + 1," + value + ")")
            self.conn.commit()
            return 1
        except:
            return None

    def ModUser(self, table, value, id, username):
        try:
            if id != 'None':
                sql = "UPDATE " + table + " SET password='" + str(value['password']) + "',is_admin='" \
                      + str(value['admin']) + "' where id='" + str(id) + "'"
                self.conn.execute(sql)
                self.conn.commit()
                return 1
            else:
                sql = "UPDATE " + table + " SET password='" + str(value['password']) + "',is_admin='" \
                      + str(value['admin']) + "' where username='" + str(username) + "'"
                self.conn.execute(sql)
                self.conn.commit()
                return 1
        except:
            return None