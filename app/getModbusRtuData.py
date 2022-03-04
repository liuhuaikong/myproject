import time
from modbus_tk import modbus_rtu
import serial
import threading
import os
import sys


mutex = threading.Lock()


# 创建moubus协议类
class modbusSensor(object):
    # 初始化modbus类,并设置需要的参数
    def __init__(self, sensor_id, sensor_name, device_descrptor, point_location, bytesize=8, baudrate=9600, parity="N", stopbits=1,
                 device_address=1):
        # threading.Thread.__init__(self)
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
        threading1 = threading.Thread(target=self.getData)
        threading1.start()

    # 创建读取点位的方法
    def getData(self):
        # 添加死循环
        while True:
            try:
                mutex.acquire()
                for k, v in self.__point_location.items():
                    function_code = v['function_code']
                    # 判断功能码
                    if function_code == 3:
                        try:
                            # 这个sleep解决了每次程序开始时,第一个传感器的第一次采集必采集不到数据,虽然解决了,但不知道为什么
                            time.sleep(1)
                            # 添加超时时间
                            self.__master.set_timeout(5.0)
                            # 不知道什么意思,猜测是同意采集数据
                            self.__master.set_verbose(True)
                            # logger = modbus_tk.utils.create_logger('console')
                            # 使用动作参数,采集数据
                            sensor_data = self.__master.execute(
                                self.__device_address, 3, v['start_address'], v['data_length'])[0]
                            # logger.info(sensor_data)
                            print(self.__sensor_name + ":" +
                                  k + ":" + str(sensor_data))
                            time.sleep(1)
                        except modbus_rtu.ModbusInvalidResponseError as e:
                            print(e)
                mutex.release()
            except Exception as e:
                print(e)
                # 输出请求帧和响应帧
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                mutex.release()
            # 每个传感器采集完睡眠一秒,防止传感器采集太慢,导致超时
            time.sleep(1)
