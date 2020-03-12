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

# 360℃までの15℃毎の値をdata配列に格納する
data_num = 15
data = []
while data_num < 375:
    data.append(data_num)
    data_num += 15

for value in data:
    msg = "---　{}゜---"
    print(msg.format(value))
    call.callofnum(value) 