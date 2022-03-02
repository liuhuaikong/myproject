from doctest import master
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
        self.__master = modbus_rtu.RtuMaster(serial.Serial(port=self.__port, bytesize=self.__bytesize,
                                                           baudrate=self.__baudrate, parity=self.__parity, stopbits=self.__stopbits))

    # 创建读取点位的方法
    def getData(self):
        for k, v in self.__point_location.items():
            function_code = v['function_code']
            if function_code == 3:
                self.__master.set_timeout(5.0)
                self.__master.set_verbose(True)
                sensor_data = self.__master.execute(
                    self.__device_address, cst.READ_HOLDING_REGISTERS, v['start_address'], v['data_length'])[0]
                print(self.__sensor_name + ":" + k + ":" + str(sensor_data))
