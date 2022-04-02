#! -*-coding:utf-8-*-
import sqlite3


class Database(object):
    def __init__(self, sensor_name, sensor_data) -> None:
        self.__sensor_name = sensor_name
        self.__sensor_data = sensor_data
        # self.__conn = self.CreateModbusdb()
        self.__conn = sqlite3.connect('modbus.db')

    def CreateModbusdb():
        conn = sqlite3.connect('modbus.db')
        print('数据库打开成功')
        c = conn.cursor()
        c.execute('''
            CREATE TABLE humiture(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                sensor_data TEXT
            );''')
        c.execute('''
            CREATE TABLE noise(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                sensor_data TEXT
            );''')
        print('数据库创建成功')
        conn.commit()
        return conn

    def InsterModbusdb(self):
        self.__conn.cursor()
        self.__conn.execute("INSERT INTO %s(sensor_data) VALUES ('%s')" %(self.__sensor_name, self.__sensor_data))
        self.__conn.commit()
        print("数据插入成功")

    def __del__(self):
        self.__conn.close()


if __name__ == "__main__":
    Database.CreateModbusdb()
