#! -*-coding:utf-8-*-
import sqlite3


class Database(object):
    def __init__(self) -> None:
        self.__conn = self.CreateModbusdb()

    def CreateModbusdb():
        conn = sqlite3.connect('modbus.db')
        print('数据库打开成功')
        c = conn.cursor()
        c.execute('''
            CREATE TABLE humiture(
                id INT PRIMARY KEY NOT NULL,
                humidity TEXT,
                temperature TEXT
            );''')
        c.execute('''
            CREATE TABLE noise(
                id INT PRIMARY KEY NOT NULL,
                noise TEXT
            );''')
        print('数据库创建成功')
        conn.commit()
        return conn

    def InsterModbusdb(self, table_name, sensor_data):
        self.__conn.execute(
            'INSERT INTO %s (%s, %s) VALUES (%s, %s)' % (table_name, sensor_data, sensor_data, sensor_data, sensor_data))
        self.__conn.commit()
        print("数据插入成功")

    def __del__(self):
        self.__conn.close()


# if __name__ == "__main__":
#     Database.CreateModbusdb()
