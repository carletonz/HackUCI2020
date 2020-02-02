import pigpio

class motor:
    def __init__(self, in1, in2, pwm, pi):
        self.in1 = in1
        self.in2 = in2
        self.pwm = pwm

        self.pi = pi

        self.pi.set_mode(self.in1, pigpio.OUTPUT)
        self.pi.set_mode(self.in2, pigpio.OUTPUT)
        self.pi.set_mode(self.pwm, pigpio.OUTPUT)
        
        self.pi.set_PWM_frequency(self.in1, 50)
        self.pi.set_PWM_frequency(self.in2, 50)

        self.pi.write(self.pwm, 1)

        print("range", self.in1, self.pi.get_PWM_frequency(self.in1))
        print("range", self.in2, self.pi.get_PWM_frequency(self.in2))

    def setSpeed(self, speed=0):
        if speed < -1:
            speed = -1
        elif speed > 1:
            speed = 1

        if speed == 0:
            self.pi.set_PWM_dutycycle(self.in1, 255)
            self.pi.set_PWM_dutycycle(self.in2, 255)
        else:
            dutyCycle = int(abs(speed) * 255)
            if speed < 0:
                print("Backwards: ", speed, dutyCycle)
                self.pi.set_PWM_dutycycle(self.in1, 0)
                self.pi.set_PWM_dutycycle(self.in2, dutyCycle)
            else:
                print("Forwards: ", speed, dutyCycle)
                self.pi.set_PWM_dutycycle(self.in1, dutyCycle)
                self.pi.set_PWM_dutycycle(self.in2, 0)

