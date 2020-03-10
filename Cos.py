# coding:utf-8
import math

class Cos():
 
    def numofCos(self, num):
        cos = math.cos(math.radians(num))
        msg = "cos{}゜= {}"
        print(msg.format(num,(round(cos,3))))
 