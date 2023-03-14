import numpy as num
import queue as priority


boundry = []
def obstacle_space(space):
    h,w,_ = space.shape
    for l in range(h):
        for m in range(w):
            if ((250-l) - 3 < 0) or ((m) - 3 < 0) or ((250-l) - 247 > 0) or ((m) - 597 > 0): #boundary
                space[l][m] = [0,0,255]
            if (m > 95) and (m < 155) and (250-l < 105) and (250-l >2):
                space[l][m] = [0,255,0]
            if (m > 100) and (m < 151) and (250-l < 101) and (250-l > 2):   #rectangle1
                space[l][m] = [0,0,255]
                boundry.append((m,250-l))
            if(m > 95) and (m < 155) and (250-l >145) and (250-l < 248):
                space[l][m] = [0,255,0]
            if (m > 100) and (m < 151) and (250-l >150) and (250-l < 248):  #rectangle2
                space[l][m] = [0,0,255]
                boundry.append((m,250-l))
            if (((0.577*m)+(250-l)-217.432)>=0) and ((m-230.048)>=0) and (((-0.577*m) + (250-l)-32.567)<=0) and (((0.577*m)+(250-l)- 378.979)<=0) and ((m-369.951)<=0) and (((-0.577*m)+(250-l)+128.980)>=0):
                space[l][m] = [0,255,0]
            if (((9375*m)+(16238*(250-l))-3624400)>=0) and (((125*m)-29381)>=0) and (((9375*m)-(16238*(250-l))+435100)>=0) and (((37500*m)+(64951*(250-l))-24240200)<=0) and (((1000*m)-364951)<=0) and (((37500*m)-(64951*(250-l))-8002450)<=0):   #hexagon
                space[l][m] = [0,0,255]
                boundry.append((m,250-l))
            if ((m-455)>=0) and (((2*m)+(250-l)-1156.18)<=0) and (((2*m)-(250-l)-906.18)<=0) and ((250-l)>20) and ((250-l)<230):
                space[l][m] = [0,255,0]
            if (((m-460)>=0)) and(((2*m)+(250-l)-1145)<=0)and (((2*m)-(250-l)-895)<=0): #triangle
                space[l][m] = [0,0,255]
                boundry.append((m,250-l))
    return (space)

blocks = []
start_node = []
end_node = []
def people_choices_begin(blocks):
    while True:
        x = (int(input("Enter the X coordinates(start): ")))
        y = (int(input("Enter the Y coordinates(start): ")))
        if (x>=0)or (x>=600) and (y>=0) (y>=250):
            if (x, y) not in blocks:
                start_node = (x,y)
                return start_node
            else:
                print("Unforunately this is inside the blocks")
        return start_node

def people_choices_end(blocks):
    while True:
        x = (int(input("Enter the X coordinates(end): ")))
        y = (int(input("Enter the Y coordinates(end): ")))
        if (x>=0)or (x>=600) and (y>=0) (y>=250):
            if (x, y) not in blocks:
                end_node = (x,y)
                return end_node
            else:
                print("Unforunately this is inside the blocks")

mage = num.ones(600,250,3)
obstacle_space(map)
