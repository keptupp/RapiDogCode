from mpu6050 import mpu6050
from time import sleep

if __name__=='__main__':
    mpu = mpu6050(0x68)
    for i in range(10000):
        print('温度：',mpu.get_temp())
        accel_data = mpu.get_accel_data()
        print('加速度：',accel_data)
        
        gyro_data = mpu.get_gyro_data()
        print('角速度：',gyro_data)
        sleep(0.5)