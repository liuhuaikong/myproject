from doctest import master
import time
from modbus_tk import modbus_rtu
import serial
import modbus_tk.defines as cst


# 创建moubus协议类
class modbusSensor(object):
    # 初始化modbus类,并设置需要的参数
    def __init__(self, sensor_id, sensor_name, device_descrptor, point_location, bytesize=8, baudrate=9600, parity="N", stopbits=1,
                 device_address=1):
        self.__sensor_id = sensor_id
        self.__sensor_name = sensor_name
        self.__port = device_descrptor
        self.__point_location = point_location
        self.__bytesize = bytesize
        self.__baudrate = baudrate
        self.__parity = parity
        self.__stopbits = stopbits
        self.__device_address = device_address
        # 建立modbus_rtu协议的通信
        self.__master = modbus_rtu.RtuMaster(serial.Serial(port=self.__port, bytesize=self.__bytesize,
                                                           baudrate=self.__baudrate, parity=self.__parity, stopbits=self.__stopbits))

    # 创建读取点位的方法
    def getData(self):
        for k, v in self.__point_location.items():
            function_code = v['function_code']
            # 判断功能码
            if function_code == 3:
                function_code == cst.READ_HOLDING_REGISTERS
                # 添加超时时间
                self.__master.set_timeout(5.0)
                # 不知道什么意思,猜测是同意采集数据
                self.__master.set_verbose(True)
                # 使用动作参数,采集数据
                sensor_data = self.__master.execute(
                    self.__device_address, function_code, v['start_address'], v['data_length'])[0]
                print(self.__sensor_name + ":" + k + ":" + str(sensor_data))
        # 每个传感器采集完睡眠一秒,防止传感器采集太慢,导致超时
        time.sleep(1)
