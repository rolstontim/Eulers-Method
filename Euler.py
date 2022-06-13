# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 18:15:01 2021

@author: Tim Rolston #V00920780
"""
import math

def Euler(m,c,g,t0,v0,tn,n):
    
    print("Values of t approximations v(t)")
    
    h = (tn - t0) / n
    t = t0
    v = v0
    
    with open("Euler_output_1b).txt", "w") as f:
        
    
        f.write("Function Called: Euler("+str(m)+","+str(c)+","+str(g)+","+str(t0)+","+str(v0)+","+str(tn)+","+str(n)+")\n\n")    
        #f.write("\nValues of t approximations v(t)\n" + format(t, '.f2') + "   " + format(v, '.4f') + "\n")
    
        for i in range(int(n)):
            
            v = v+(g-c/m*v)*h
            t = t + h
            #print(round(t, 2), round(v, 4))
            f.write("t: " + format(t, '.2f') + "   " + "v(t): " + format(v, '.4f') + "\n")
            
        x = ((c*t)/m)  
        ans = ((g*m)/c)*(1-(math.e**(-x)))
        
        relative_error = abs((ans - v)/ans)
        f.write("\nRelative Error: " + str(relative_error) + "\n")
        
        
def Euler2(m,k,g,t0,v0,tn,n):
    
    h = (tn - t0) / n
    t = t0
    v = v0
    
    with open("Euler2_output_2).txt", "w") as f:
        
        f.write("Function Called: Euler2("+str(m)+","+str(k)+","+str(g)+","+str(t0)+","+str(v0)+","+str(tn)+","+str(n)+")\n\n") 
        
        for i in range(int(n)):
            
            v = v+(g-((k/m)*(v**2)))*h
            t = t + h
            #print(round(t, 2), round(v, 4))
            f.write("t: " + format(t, '.2f') + "   " + "dv/dt: " + format(v, '.4f') + "\n")
        
        ans = math.sqrt((g*m)/k)*(math.tanh(math.sqrt((g*k)/m)*t))
        relative_error = abs((ans - v)/ans)
        f.write("\nRelative_Error: " + str(relative_error))
        

def McLaurin(x):
    
    e_exp_x1 = 0
    e_exp_x2 = 0
    e = math.e**(x)
    n = 0
    
    #for the first approach
    for n in range(6 + 1):
                
        e_exp_x1 += ((x**n)/math.factorial(n))
                
    relative_error_1 = abs((e - e_exp_x1) / e)
    
    #for the second approach
    x = x*-1
    for n in range(6 + 1):
        
        e_exp_x2 += ((x**n)/math.factorial(n))
        
    e_exp_x2 = 1/e_exp_x2
    relative_error_2 = abs((e - e_exp_x2) / e)
    
    with open("McLaurin_output_3).txt", "w") as f:
        
        f.write("Function Called: McLaurin(" + str(x) + ")\n\n")
        f.write("approach one: " + format(e_exp_x1, '.4f') + "= e**" + str(x) + "\n" + "relative error: " + format(relative_error_1, '.4f') + "\n\n")
        f.write("apprach two: " + format(e_exp_x2, '.4f') + "= e**" + str(x) + "\n" + "relative error: " + format(relative_error_2, '.4f'))
        
        
def main():
    
    equation = input("What equation?; Euler1, Euler2, McLaurin: ")
    
    if (equation == "Euler1"):

        print("this is a program to calculate Euler's method")
        m = float(input("enter value for mass \'m': "))
        c = float(input("enter value for drag coefficient \'c': "))
        g = float(input("enter value for gravity constant \'g': "))
        t0 = float(input("enter value for initial time \'t0': "))
        tn = float(input("enter value for final time \'tn': "))
        v0 = float(input("enter value for initial velocity \'v0': "))
        n = float(input("enter value for number of time steps [t0,tn] is divided \'n': "))
        Euler(m,c,g,t0,v0,tn,n)
    
    elif (equation == "Euler2"):
        
        print("this is a program to calculate Euler's method alternatively")
        m = float(input("enter value for mass \'m': "))
        k = float(input("enter value for second-order drag coefficient \'k': "))
        g = float(input("enter value for gravity constant \'g': "))
        t0 = float(input("enter value for initial time \'t0': "))
        tn = float(input("enter value for final time \'tn': "))
        v0 = float(input("enter value for initial velocity \'v0': "))
        n = float(input("enter value for number of time steps [t0,tn] is divided \'n': "))
        Euler2(m,k,g,t0,v0,tn,n)

    elif (equation == "McLaurin"):
        
        print("this is a program to calculate a McLaurin series")
        x = float(input("enter value for e^\'x': "))
        McLaurin(x)
    else:
        print("invalid syntax of function entered or not supported")
        return
    
    return


if __name__ =="__main__":
    main()

