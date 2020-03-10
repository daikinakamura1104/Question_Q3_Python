# coding:utf-8
import Sin
import Cos
import Tan


class Call():
 
    def callofnum(self,num):
        sin.numofSin(num)
        cos.numofCos(num)
        tan.numofTan(num)

# インスタンス化する
sin = Sin.Sin()
cos = Cos.Cos()
tan = Tan.Tan()
call = Call()

data = [15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345,360]
for value in data:
    msg = "---　{}゜---"
    print(msg.format(value))
    call.callofnum(value)