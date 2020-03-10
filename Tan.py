# coding:utf-8
import math

class Tan():
 
    def numofTan(self, num):
        tan = math.tan(math.radians(num))
        msg = "tan{}゜= {}"
        print(msg.format(num,(round(tan,3))))