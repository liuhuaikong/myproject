#!/usr/bin/env python3
#! -*-coding:utf-8-*-
import click
from .GetModbusRtuData import ModbusSensor
import json


# 创建一个装饰器
@click.command()
# 设置command对象的参数
@click.option('--file', type=click.Path(), help='请上传JSON文件')
# 解析传入的参数
def cli(file):
    try:
        # 使用utf8编码格式读传入的文件
        with open(file, 'r', encoding='utf8') as f:
            # 使用json.load将文本文件解析为字典类型
            json_data = json.load(f)
            # 遍历json文件中的所有传感器
            for k in json_data:
                profile = {}
                # 从字典中取需要的数据,并断言数据类型
                sensor_name = json_data[k]['sensor_name']
                profile["sensor_name"] = sensor_name
                assert isinstance(sensor_name, str)
                agreement = json_data[k]['agreement']
                assert isinstance(agreement, str)
                device_descrptor = json_data[k]['communication']['port']
                assert isinstance(device_descrptor, str)
                bytesize = json_data[k]['communication']['bytesize']
                assert isinstance(bytesize, int)
                baudrate = json_data[k]['communication']['baudrate']
                assert isinstance(baudrate, int)
                parity = json_data[k]['communication']['parity']
                assert isinstance(parity, str)
                stopbits = json_data[k]['communication']['stopbits']
                assert isinstance(stopbits, int)
                device_address = json_data[k]['communication']['device_address']
                assert isinstance(device_address, int)
                point_location = json_data[k]["point_location"]
                assert isinstance(point_location, dict)
                # 如果传感器是modbus_rtu协议,调用modbusSensor类的getData方法,并将所有参数传给modbusSensor类里
                if agreement == 'modbus_rtu':
                    ModbusSensor(sensor_name, device_descrptor, point_location, bytesize, baudrate, parity, stopbits,
                                 device_address)
    except Exception as e:
        print(e)
