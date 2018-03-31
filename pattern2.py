# importing library
import os
import time
def solveCir(y,r):
    x = r**2 - y **
    
def circle(r):
    d = 2 * r
    cir = [[0 for x in range(d)] for y in range()]
    for i in range(d):
        line = " "
        for j in range(d):
            if 
            cir[i][j] = "* "
            line += cir[i][j]
        print(line)


# Triangle function.
# pattern no 2
def tri(n):   
    for i in range(0, n+1):
        if i%2 == 1:
            for j in range(1, i+1):
                if j < 10:
                    print("*",end=" ")
                else:
                    print("* ",end=" ")
        if i%2 == 0:
            for k in range(1, i+1):
                 print(k,end=" ")
        print("\r")        


# square function.
# pattern no 1
def sqr(n) :
    for i in range(1,n):
        if i == 1:
            for j in range(1,n+1):
                print("*",end=" ")    
            print("\r")
        if i == n-1:
            for j in range(1,n+1):
                print("*",end=" ")    
            print("\r")
        else:
            for k in range(1,n+1):
                if k == 1:
                    print("*", end=" ")
                if k == n-1:
                    print("*", end=" ")
                else:
                    print(" ",end=" ")
            print("\r")


# Triangle2 progran.
def revtri(n):
    for i in range(n):
        if n < 10:
            if i%2 == 0:
                for j in range(n):
                    if j < (n-i-1):
                        print(" ",end=" ")
                    else:
                        print("*",end=" ")
            else:
                temp = 1
                for j in range(n):
                    
                    if j <(n-i-1):
                        print(" ",end=" ")
                    else:
                        print(temp,end=" ")
                        temp += 1
        else:
            if i%2 == 0:
                for j in range(n):
                    
                    if j < (n-i-1):
                        print("  ",end=" ")
                    else:
                        print("* ",end=" ")
            else:
                temp = 1
                for j in range(n):
    
                    if j <(n-i-1):
                        print("  ",end=" ")
                    else:
                        if temp < 10:
                            print(temp,end="  ")
                        else:
                            print(temp,end=" ")
                        temp += 1
        print("\r")
        


    
# main program
start = 1
while start == 1:
    print("This is pattern making software:")
    print("<1> for square :")
    print("<2> for triangle :")
    print("<3> for triangle2 :")
    print("<4> for growing square :")
    print("<5> for circle : ")
    print("<6> Exit")
    data = int(input("Enter choice : "))
    if data == 1:
        size = int(input("Enter Size   : "))
        os.system('cls')
        sqr(size)
    elif data == 2:
        size = int(input("Enter Size   : "))
        os.system('cls')
        tri(size)
    elif data == 3:
        size = int(input("Enter Size   : "))
        os.system('cls')
        revtri(size)
    elif data == 4:
        size = int(input("Enter Size : "))
        os.system('cls')
        for i in range(size):
            sqr(i+1)
            time.sleep(0.05)
            os.system('cls')
    elif data == 5:
        size = int(input("Enter Size : "))
        os.system('cls')
        circle(size)
        
    elif data == 6:
        start = 0
    else :
        os.system("cls")
        print("*****************Enter a valid key*******************")
