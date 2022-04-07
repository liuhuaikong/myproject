#!/usr/bin/env python3
#! -*-coding:utf-8-*-
from flask import Flask
import json
import sys
# sys.path.append('/home/senscape/python_click_modbus/app')
from app.databases import Database


app = Flask(__name__)


class Api(object):
    def __init__(self):
        pass

    # 查询所有的物模型
    @app.route('/SensorModel', methods=['GET'])
    def GetSensorModel():
        with open('../test/test.json', 'r', encoding='utf8') as f:
            # 使用json.load将文本文件解析为字典类型
            json_data = json.load(f)
            return json_data

    # 根据传感器名称查询物模型
    @app.route('/SensorModel/<string:sensor_name>', methods=['GET'])
    def GetSensorModelId(sensor_name):
        with open('./test/test.json', 'r', encoding='utf8') as f:
            # 使用json.load将文本文件解析为字典类型
            json_data = json.load(f)
            sensor_model = json_data[sensor_name]
            return sensor_model

    # 根据传感器名称查询历史
    @app.route('/SensorData/<string:sensor_name>', methods=['GET'])
    def GetSensorData(sensor_name):
        print(sensor_name)
        sensor_data = Database(sensor_name).SelectTable()
        return sensor_data

    app.run()
