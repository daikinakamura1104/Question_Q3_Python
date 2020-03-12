# coding:utf-8
import math


class Angle():
 
    def callofnum(self,num):
        msg = "sin{}゜=　{}"
        val = math.sin(math.radians(num))
        print(msg.format(num,round(val,2)))
        msg = "cos{}゜=　{}"
        val = math.cos(math.radians(num))
        print(msg.format(num,round(val,2)))
        msg = "tan{}゜=　{}"
        val = math.tan(math.radians(num))
        print(msg.format(num,round(val,2)))
        

angle = Angle()

data_num = 15
data = []
while data_num <= 360:
    data.append(data_num)
    data_num += 15

for value in data:
    msg = "---　{}゜---"
    print(msg.format(value))
    angle.callofnum(value) 