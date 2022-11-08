from math import sqrt
import numpy as np
from sympy import *

y = symbols('y', cls=Function)
x = symbols('x')
c1 = symbols('C1')
c2 = symbols('C2')
string_math = None

def model(t, z):
    #from math import sqrt
    global string_math, y, x
       
    return sympify(string_math).evalf(subs={y(x):z, x:t})


def RK1(F, Xo, Xf, Yo, n, string, step, const1):
    global string_math, y, x
    
    """ RK values """
    string_math = string
    solution = dsolve(Eq(y(x).diff(x) - sympify(string_math), 0), y(x))
    
    #h = (Xf - Xo)/n
    h = step
    mask = np.zeros((n, 4))
    
    real_data = np.zeros((1,n))
    for i in range(0, n, 1):
        if i == 0:
            temp = mask[i]
            temp[0] = i
            temp[1] = Xo
            temp[2] = Yo
            
            dy = temp[2] + (h*F(temp[1], temp[2]))
            temp[3] = dy
            real_data[0][i] = solution.evalf(subs={c1:const1, x:temp[1]}).args[1]
                
        else:
            temp = mask[i]
            temp[0] = i
            temp[1] = mask[i-1][1] + h
            temp[2] = mask[i-1][3]
            
            dy = temp[2] + (h*F(temp[1], temp[2]))
            temp[3] = dy
            real_data[0][i] = solution.evalf(subs={c1:const1, x:temp[1]}).args[1]
            
    return mask, real_data

def RK2(F, Xo, Xf, Yo, n, step, const1):
    mask = np.zeros((n, 6))
    #h = (Xf - Xo)/n
    h = step
    
    for i in range(0, n, 1):
        if i == 0:
            temp = mask[i]
            temp[0] = i
            temp[1] = Xo
            temp[2] = Yo
            
            temp[3] = k1 = h * F(temp[1], temp[2])
            temp[4] = k2 = h * F(temp[1] + h, temp[2] + k1)
            
            dy = temp[2] + ((1/2) * (k1+k2))
            temp[-1] = dy
            
        else:
            temp = mask[i]
            temp[0] = i
            temp[1] = mask[i-1][1] + h
            temp[2] = mask[i-1][-1]
            
            temp[3] = k1 = h * F(temp[1], temp[2])
            temp[4] = k2 = h * F(temp[1] + h, temp[2] + k1)
            
            dy = temp[2] + ((1/2) * (k1+k2))
            temp[-1] = dy
    return mask
    
def RK3(F, Xo, Xf, Yo, n, step, const1):
    
    mask = np.zeros((n, 7))
    
    h = step
    
    for i in range(0, n, 1):
        if i == 0:
            temp = mask[i]
            temp[0] = i
            temp[1] = Xo
            temp[2] = Yo
            
            temp[3] = k1 = F(temp[1], temp[2])
            temp[4] = k2 = F(temp[1] + (h/2), temp[2] + ((h/2)*k1))
            temp[5] = k3 = F(temp[1] + h, (temp[2] - (h*k1) + (2*h*k2)))
            
            dy = temp[2] + ((h/6)*(k1 + (4*k2) + k3))
            temp[-1] = dy
            
        else:
            temp = mask[i]
            temp[0] = i
            temp[1] = mask[i-1][1] + h
            temp[2] = mask[i-1][-1]
            
            temp[3] = k1 = F(temp[1], temp[2])
            temp[4] = k2 = F(temp[1] + (h/2), temp[2] + ((h/2)*k1))
            temp[5] = k3 = F(temp[1] + h, temp[2] - (h*k1) + (2*h*k2))
            
            dy = temp[2] + ((h/6)*(k1 + (4*k2) + k3))
            temp[-1] = dy
    return mask

def RK4(F, Xo, Xf, Yo, n, step, const1):
    
    mask = np.zeros((n, 8))
    
    h = step
    
    for i in range(0, n, 1):
        if i == 0:
            temp = mask[i]
            temp[0] = i
            temp[1] = Xo
            temp[2] = Yo
            
            temp[3] = k1 = F(temp[1], temp[2])
            temp[4] = k2 = F(temp[1] + (h/2), temp[2] + ((h/2)*k1))
            temp[5] = k3 = F(temp[1] + (h/2), temp[2] + ((h/2)*k2))
            temp[6] = k4 = F(temp[1] + h, temp[2] + (h*k3))
            
            dy = temp[2] + ((h/6)*(k1 + (2*k2) + (2*k3) + k4))
            temp[-1] = dy
            
        else:
            temp = mask[i]
            temp[0] = i
            temp[1] = mask[i-1][1] + h
            temp[2] = mask[i-1][-1]
            
            temp[3] = k1 = F(temp[1], temp[2])
            temp[4] = k2 = F(temp[1] + (h/2), temp[2] + ((h/2)*k1))
            temp[5] = k3 = F(temp[1] + (h/2), temp[2] + ((h/2)*k2))
            temp[6] = k4 = F(temp[1] + h, temp[2] + (h*k3))
            
            dy = temp[2] + ((h/6)*(k1 + (2*k2) + (2*k3) + k4))
            temp[-1] = dy
    return mask

Xo = 1
Yo = 4
Xf = 1.6
n = 3

#result_rk1 = rungeKutta1(model, Xo, Xf,Yo, n)
#result_rk2 = rungeKutta2(model, Xo, Xf, Yo, n)
#result_rk3 = rungeKutta3(model, Xo, Xf, Yo, n)
#result_rk4 = rungeKutta4(model, Xo, Xf, Yo, n)
#print(result_rk4)        
        