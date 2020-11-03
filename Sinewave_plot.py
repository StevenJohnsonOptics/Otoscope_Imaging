import numpy as np

"""Ive created 3 phase maps sinusoidally varying from 0 to 255 but when i 
plot them they arent in gray scale and im not sure how to do that but these 
are the current 3 phase maps """

w=(2*np.pi)/50 
Px1 = [] 
for i in range(800): 
    Px1.append(127.5*np.sin((w*(i+1))+127.5)) 
    repetitions = 600 
    px1 = np.tile(Px1,(repetitions,1))

Px2 = [] 
for i in range(800): 
    Px2.append(127.5*np.sin(w*(i+1)+(2*np.pi/3))+127.5) 
    repetitions = 600 
    px2 = np.tile(Px2,(repetitions,1))

Px3 = [] 
for i in range(800): 
    Px3.append(127.5*np.sin(w*(i+1)+(4*np.pi/3))+127.5)
    repetitions = 600 
    px3 = np.tile(Px3,(repetitions,1))

"""building code for the combining of the images and the object for the phase
 #possibly lazy way of getting the ith value for the x coordinate """
x = [] 
for i in range(800): 
    x.append(i+1) 
    repetitions = 600 
    x1 = np.tile(x,(repetitions,1)) 
    print(x1) #the object 
    Height = 1

obj = np.zeros((800,600))

obj[4:14,4:12] = Height 
print(obj)

#then the equations started but need some clarifying 
"""
Ixy = IIxy = o1 = (wx)+obj 
o2 = (wx)+obj+((2np.pi)/3) 
o3 = (wx)+obj+((4np.pi)/3) 
I1 = Ixy +(IIxy(cos(o1))) 
I2 = Ixy +(IIxy*(cos(o2))) 
I3 = Ixy +(IIxy*(cos(o3))) 
oxy = atan(sqrt(3)(I1-I3)/((2*I2)-I1-I3))
"""