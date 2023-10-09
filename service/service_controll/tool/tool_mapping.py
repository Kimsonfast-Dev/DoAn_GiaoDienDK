import numpy as np
import random

class mapping():
    def __init__(self,xp,yp) -> None:
        self.list_check = []
        self.x_point = xp
        self.y_point = yp 
        None

    def input_list(self,value):
        self.point = value

    def update_listcheck(self):
        self.list_check = []
        width = self.x_point - 1
        height = self.y_point - 1
        var = []
        count = 0
        hello = -1
        for i in range((width+1)*(height)):
            if(i%width==0 and i != 0):
                hello = i+count
                count = count + 1
                if(count>width): count = 0
            if(i!=hello):
                var.append([i,width+i+1,i+width+2])
                var.append([i,i+1,i+width+2])
        
        print(len(var))

        for index in var:
            self.list_check.append([self.point[index[0]],self.point[index[1]],self.point[index[2]]])



    def check_inside(self,point1,point2,point3,xp,yp):
        x1 = point1[0]
        y1 = point1[1]
        x2 = point2[0]
        y2 = point2[1]
        x3 = point3[0]
        y3 = point3[1]
        output = -1
        c1 = (x2-x1)*(yp-y1)-(y2-y1)*(xp-x1)
        c2 = (x3-x2)*(yp-y2)-(y3-y2)*(xp-x2)
        c3 = (x1-x3)*(yp-y3)-(y1-y3)*(xp-x3)
        if (c1<=0 and c2<=0 and c3<=0) or (c1>=0 and c2>=0 and c3>=0):
            output = 1
        else:
            output = 0
        return output

    def check_mapping(self,pointA,pointB,pointC,x,y):
        v1 = np.array(pointB) - np.array(pointA)
        v2 = np.array(pointC) - np.array(pointA)
        n = np.cross(v1, v2)
        z = -(n[0]*(x-pointA[0]) + n[1]*(y-pointA[1]))/n[2] + pointA[2]
        if(z>max([pointA[2],pointB[2],pointC[2]]) or z<min([pointA[2],pointB[2],pointC[2]])):
            z =-1
        return z
    
    def check_full(self,x,y):
        output = -1
        for data in self.list_check:
            if(self.check_inside(data[0],data[1],data[2],x,y)>0):
                output = self.check_mapping(data[0],data[1],data[2],x,y)
        return output