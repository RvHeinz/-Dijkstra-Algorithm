import numpy as num
import cv2 
from queue import PriorityQueue as PQ
#import heapq as q

v_nodes = PQ()
un_nodes = []
limits = []
track ={}
def hindrance(mage):
    h,w,_ = mage.shape
    for l in range(h):
        for m in range(w):
            if ((250-l) - 3 < 0) or ((m) - 3 < 0) or ((250-l) - 247 > 0) or ((m) - 597 > 0): #boundary
                mage[l][m] = [0,0,255]
            if (m > 95) and (m < 155) and (250-l < 105) and (250-l >2):
                mage[l][m] = [0,255,0]
            if (m > 100) and (m < 151) and (250-l < 101) and (250-l > 2):   #rectangle1
                mage[l][m] = [0,0,255]
                limits.append((m,250-l))
            if(m > 95) and (m < 155) and (250-l >145) and (250-l < 248):
                mage[l][m] = [0,255,0]
            if (m > 100) and (m < 151) and (250-l >150) and (250-l < 248):  #rectangle2
                mage[l][m] = [0,0,255]
                limits.append((m,250-l))
            if (((0.577*m)+(250-l)-217.432)>=0) and ((m-230.048)>=0) and (((-0.577*m) + (250-l)-32.567)<=0) and (((0.577*m)+(250-l)- 378.979)<=0) and ((m-369.951)<=0) and (((-0.577*m)+(250-l)+128.980)>=0):
                mage[l][m] = [0,255,0]
            if (((9375*m)+(16238*(250-l))-3624400)>=0) and (((125*m)-29381)>=0) and (((9375*m)-(16238*(250-l))+435100)>=0) and (((37500*m)+(64951*(250-l))-24240200)<=0) and (((1000*m)-364951)<=0) and (((37500*m)-(64951*(250-l))-8002450)<=0):   #hexagon
                mage[l][m] = [0,0,255]
                limits.append((m,250-l))
            if ((m-455)>=0) and (((2*m)+(250-l)-1156.18)<=0) and (((2*m)-(250-l)-906.18)<=0) and ((250-l)>20) and ((250-l)<230):
                mage[l][m] = [0,255,0]
            if (((m-460)>=0)) and(((2*m)+(250-l)-1145)<=0)and (((2*m)-(250-l)-895)<=0): #triangle
                mage[l][m] = [0,0,255]
                limits.append((m,250-l))
    return (limits)




def people_choices_begin(val):
    while True:
        x = int(input("Enter the X coordinates(start): "))
        y = int(input("Enter the Y coordinates(start): "))
        if (x>=0)or (x<=600) and (y>=0)or (y<=250):
            if (x, y) not in val:
                start_node = (x,y)
                return start_node
            else:
                print("Unforunately this is inside the blocks, please enter a correct value")
        else:
            print("Enter the value as per the image/grid size")
        

def people_choices_end(val):
    while True:
        x = int(input("Enter the X coordinates(end): "))
        y = int(input("Enter the Y coordinates(end): "))
        if ((x>=0)or (x<=600)) and ((y>=0) or (y<=250)):
            if (x, y) not in val:
                end_node = (x,y)
                return end_node
            else:
                print("Unforunately this is inside the blocks, please enter a correct value")
        else:
            print("Enter the value as per the image/grid size")
def up(v, un_nodes):
    old_spot = v[1]
    new_spot = (old_spot[0],old_spot[1]+1)
    if (new_spot not in un_nodes) and (new_spot not in limits):
        Cost = v[0] + 1
        for m in range(v_nodes.qsize()):
            if v_nodes.queue[m][1] == new_spot:
                if v_nodes.queue[m][0] > Cost:
                    v_nodes.queue[m] = (Cost,new_spot)
                    track[new_spot] = old_spot
                    return
                else:
                    return
        v_nodes.put((Cost,new_spot))
        track[new_spot] = old_spot 

def down(v, un_nodes):
    old_spot = v[1]
    new_spot = (old_spot[0],old_spot[1]-1)
    if (new_spot not in un_nodes) and (new_spot not in limits):
        Cost = v[0] + 1
        for m in range(v_nodes.qsize()):
            if v_nodes.queue[m][1] == new_spot:
                if v_nodes.queue[m][0] > Cost:
                    v_nodes.queue[m] = (Cost,new_spot)
                    track[new_spot] = old_spot
                    return
                else:
                    return
        v_nodes.put((Cost,new_spot))
        track[new_spot] = old_spot

def left(v, un_nodes):
    old_spot = v[1]
    new_spot = (old_spot[0]-1,old_spot[1])
    if (new_spot not in un_nodes) and (new_spot not in limits):
        Cost = v[0] + 1
        for m in range(v_nodes.qsize()):
            if v_nodes.queue[m][1] == new_spot:
                if v_nodes.queue[m][0] > Cost:
                    v_nodes.queue[m] = (Cost,new_spot)
                    track[new_spot] = old_spot
                    return
                else:
                    return
        v_nodes.put((Cost,new_spot))
        track[new_spot] = old_spot

def right(v, un_nodes):
    old_spot = v[1]
    new_spot = (old_spot[0]+1,old_spot[1])
    if (new_spot not in un_nodes) and (new_spot not in limits):
        Cost = v[0] + 1
        for m in range(v_nodes.qsize()):
            if v_nodes.queue[m][1] == new_spot:
                if v_nodes.queue[m][0] > Cost:
                    v_nodes.queue[m] = (Cost,new_spot)
                    track[new_spot] = old_spot
                    return
                else:
                    return
        v_nodes.put((Cost,new_spot))
        track[new_spot] = old_spot

def downright(v,un_nodes):
    old_spot = v[1]
    new_spot = (old_spot[0]-1,old_spot[1]+1)
    if (new_spot not in un_nodes) and (new_spot not in limits):
        Cost = v[0] + 1.4
        for m in range(v_nodes.qsize()):
            if v_nodes.queue[m][1] == new_spot:
                if v_nodes.queue[m][0] > Cost:
                    v_nodes.queue[m] = (Cost,new_spot)
                    track[new_spot] = old_spot
                    return
                else:
                    return
        v_nodes.put((Cost,new_spot))
        track[new_spot] = old_spot

def downleft(v,un_nodes):
    old_spot = v[1]
    new_spot = (old_spot[0]-1,old_spot[1]-1)
    if (new_spot not in un_nodes) and (new_spot not in limits):
        Cost = v[0] + 1.4
        for m in range(v_nodes.qsize()):
            if v_nodes.queue[m][1] == new_spot:
                if v_nodes.queue[m][0] > Cost:
                    v_nodes.queue[m] = (Cost,new_spot)
                    track[new_spot] = old_spot
                    return
                else:
                    return
        v_nodes.put((Cost,new_spot))
        track[new_spot] = old_spot

def upright(v,un_nodes):
    old_spot = v[1]
    new_spot = (old_spot[0]+1,old_spot[1]+1)
    if (new_spot not in un_nodes) and (new_spot not in limits):
        Cost = v[0] + 1.4
        for m in range(v_nodes.qsize()):
            if v_nodes.queue[m][1] == new_spot:
                if v_nodes.queue[m][0] > Cost:
                    v_nodes.queue[m] = (Cost,new_spot)
                    track[new_spot] = old_spot
                    return
                else:
                    return
        v_nodes.put((Cost,new_spot))
        track[new_spot] = old_spot

def upleft(v,un_nodes):
    old_spot = v[1]
    new_spot = (old_spot[0]+1,old_spot[1]+1)
    if (new_spot not in un_nodes) and (new_spot not in limits):
        Cost = v[0] + 1.4
        for m in range(v_nodes.qsize()):
            if v_nodes.queue[m][1] == new_spot:
                if v_nodes.queue[m][0] > Cost:
                    v_nodes.queue[m] = (Cost,new_spot)
                    track[new_spot] = old_spot
                    return
                else:
                    return
        v_nodes.put((Cost,new_spot))
        track[new_spot] = old_spot

def bt(track, Begin, end):
    b_t = []
    K = track.get(end)
    b_t.append(end)
    b_t.append(K)
    while (K != Begin):  
        K = track.get(K)
        b_t.append(K)
    b_t.reverse()
    return (b_t)
mage = num.ones((250,600,3), dtype= 'uint8')
val = hindrance(mage)
Begin = people_choices_begin(val)
End = people_choices_end (val)
commence = (0, Begin)
v_nodes.put(commence)
while True:
    v = v_nodes.get()
    un_nodes.append(v[1])
    (x,y) = v[1]
    if v[1] != End:
        if (y+1< 250):
            up(v,un_nodes)
        if ((y-1) > 0):
            down(v,un_nodes)
        if ((x-1) > 0):
            left(v,un_nodes)
        if ((x+1)<600):
            right(v,un_nodes)
        if((x-1)>0) and ((y+1)<250):
            upleft(v,un_nodes)
        if((x+1)<600) and ((y+1)<250):
            upright(v,un_nodes)
        if((x-1)>0) and ((y-1)>0):
            downleft(v,un_nodes)
        if((x+1)<600) and ((y-1)>0):
            downright(v,un_nodes)    
    else:
        print("Awesome, the node has achieved the end state  ")
        break

b = bt(track, Begin, End)
print("finished")

for i in un_nodes:
    val[250-i[1]][i[0]] = [255,0,0]
    
for j in b:
    val[250-j[1]][j[0]] = [255,0,0]
    
cv2.imshow("obstacle space",val)
cv2.waitKey(0)
cv2.destroyAllWindows()