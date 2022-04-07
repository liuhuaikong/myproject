#!/usr/bin/env python3
#! -*-coding:utf-8-*-
import sqlite3


class Database(object):
    # 初始化数据库
    def __init__(self, sensor_name='', sensor_data='') -> None:
        self.__sensor_name = sensor_name
        self.__sensor_data = sensor_data
        # 打开数据库
        self.__conn = sqlite3.connect('modbus.db')
        self.__cur = self.__conn.cursor()

    # 创建表
    def CreateTable(self):
        # 如果不存在传感器表,则创建
        try:
            self.__cur.execute(
                "CREATE TABLE IF NOT EXISTS %s(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, sensor_data TEXT);" % (self.__sensor_name))
            self.__conn.commit()
            print(self.__sensor_name + '表创建成功')
        except:
            return False

    # 插入数据
    def InsterTable(self):
        try:
            self.__cur = self.__conn.cursor()
            self.__cur.execute("INSERT INTO %s(sensor_data) VALUES ('%s')" % (
                self.__sensor_name, self.__sensor_data))
            self.__conn.commit()
            print("数据插入成功")
        except:
            return False

    # 查询数据
    def SelectTable(self):
        try:
            self.__cur.execute("SELECT * FROM %s;" % (self.__sensor_name))
            sensor_data = self.__cur.fetchall()
            data_dict = {}
            for x in sensor_data:
                data_dict[(x[0])] = x[1].replace("\"","'")
            print(data_dict)
            return data_dict
        except:
            return False

    def __del__(self):
        self.__conn.close()
