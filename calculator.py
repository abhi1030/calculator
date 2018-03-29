from tkinter import *

root = Tk()


temp = ""
equation = StringVar()

def btnPress(num):
    global temp
    temp = temp + str(num)
    equation.set(temp)

def clearScr():
    global temp
    temp = ""
    equation.set(temp)

def answer():
    global temp
    y = temp.split('pi')
    if len(y) == 2:
        y[0] = y[0] + str(22/7) + y[1]
    if len(y) == 3:
        y[0] = y[0] + str(22/7) + y[1] + str(22/7) + y[2]
    if len(y) == 4:
        y[0] = y[0] + str(22/7) + y[1] + str(22/7) + y[2] + str(22/7) + y[3]
    total = str(eval(y[0]))
    
    temp = total
    equation.set(temp)

displayText = Label(root,textvariable = equation)
one = Button(root,text = "1",command = lambda:btnPress(1))
two = Button(root,text = "2",command = lambda:btnPress(2))
three = Button(root,text = "3",command = lambda:btnPress(3))
four = Button(root,text = "4",command = lambda:btnPress(4))
five = Button(root,text = "5",command = lambda:btnPress(5))
six = Button(root,text = "6",command = lambda:btnPress(6))
seven = Button(root,text = "7",command = lambda:btnPress(7))
eight = Button(root,text = "8",command = lambda:btnPress(8))
nine = Button(root,text = "9",command = lambda:btnPress(9))
zero = Button(root,text = "0",command = lambda:btnPress(0))
plus = Button(root,text = "+",command = lambda:btnPress("+"))
minus = Button(root,text = "-",command = lambda:btnPress("-"))
multiply = Button(root,text = "*",command = lambda:btnPress("*"))
divide = Button(root,text = "/",command = lambda:btnPress("/"))
point = Button(root,text = ".",command = lambda:btnPress("."))
power = Button(root,text = "^",command = lambda:btnPress("**"))
pi = Button(root,text = "π",command = lambda:btnPress("pi"))
equalto = Button(root,text = "=" , command = answer)
clearbtn = Button(root,text = "C", command = clearScr)

displayText.grid(columnspan = 4)
one.grid(row = 1 , column = 0)
two.grid(row = 1 , column = 1)
three.grid(row = 1 , column = 2)
plus.grid(row = 2 , column = 3)
four.grid(row = 2 , column = 0)
five.grid(row = 2, column = 1)
six.grid(row = 2 , column = 2)
minus.grid(row = 3 , column = 3)
seven.grid(row = 3 , column = 0)
eight.grid(row = 3 , column = 1)
nine.grid(row = 3 , column = 2)
multiply.grid(row = 4 , column = 3)
clearbtn.grid(row = 1 , column = 3)
zero.grid(row = 4 , column = 1)
equalto.grid(row = 5 , column = 0)
divide.grid(row = 5 , column = 3)
point.grid(row=4,column= 0)
power.grid(row=4,column=2)
pi.grid(row=5,column=1)


root.mainloop()
