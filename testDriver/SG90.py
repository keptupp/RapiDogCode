import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)#设置引脚编码模式
GPIO.setup(4,GPIO.OUT)#设置引脚及其模式（输出）


sg90_pwm=GPIO.PWM(4,50)#设置4号引脚为PWM，频率1s50次

sg90_pwm.start(0)#初始化占空比

#sg90_pwm.ChangeFrequency()#更新频率
sg90_pwm.ChangeDutyCycle(10)#跟新占空比

#sg90舵机频率50Hz，也就是20ms
# 0°是0.5ms，180°是2.5ms
#换算0°占空比2.5％，180°占空比12.5%
def sg90_angle(angle):
    sg90_pwm.ChangeDutyCycle(2.5+angle*10/180)

def main():
    for i in range(5):
        sg90_angle(0)
        print('启动舵机0°，等待3s')
        time.sleep(3)

        sg90_angle(90)
        print('90°，等待3s')
        time.sleep(3)

        sg90_angle(180)
        print('180°，等待3s')
        time.sleep(3)

    sg90_pwm.stop()
    GPIO.cleanup()

main()