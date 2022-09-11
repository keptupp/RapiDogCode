import pac9685

if __name__=='__main__':
    pwm = pac9685.PCA9685(0x40, debug=False)
    while(True):
        print("输入舵机")
        channel,angle=input().split()
        pwm.setAngle(int(channel),int(angle))
