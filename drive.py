from motor import motor
import pigpio

class drive:
    def __init__(self):
        self.pi = pigpio.pi()

        self.FL = motor(15, 14, 18, self.pi)
        self.FR = motor(20, 16, 21, self.pi)
        
        self.BL = motor(3, 2, 4, self.pi)
        self.BR = motor(5, 6, 13, self.pi)

        #pi.set_mode(18, pigpio.OUTPUT)
        #pi.write(18, 1)

    def left(self, speed = 0):
        self.FL.setSpeed(speed)
        self.BL.setSpeed(-speed)

    def right(self, speed = 0):
        self.FR.setSpeed(speed)
        self.BR.setSpeed(-speed)

    def forward(self, speed = 0):
        self.left(speed)
        self.right(speed)

    def turn(self, speed = 0):
        self.left(speed)
        self.right(-speed)

#d = drive()
#
#while True:
#    i = input("Command: ")
#    if i == "s":
#        break
#    elif i == "f":
#        d.forward(0.1)
#    elif i == "t":
#        d.turn(0.5)
#
#d.forward(0)
