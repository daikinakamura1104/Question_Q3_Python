# coding:utf-8
import math

class Sin():
 
    def numofSin(self, num):
        sin = math.sin(math.radians(num))
        msg = "sin{}゜=　{}"
        print(msg.format(num,(round(sin,3))))
 


