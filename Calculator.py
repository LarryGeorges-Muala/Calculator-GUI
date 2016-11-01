#App Name: Simple Python Calculator GUI
#Python Version 3.5
#Developper: Larry Georges Muala

import tkinter
from tkinter import messagebox

window = tkinter.Tk()

window.title('Simple Python Calculator')

#Disable maximize button
window.resizable(0,0)

#Modify window icon
window.wm_iconbitmap('lelu.ico')

#Set window background color
window.configure(background="gray2")



#Menu Bar

def about_app():
	print("App Name: Simple Python Calculator GUI")
	print("App Description: Calculator GUI doing addition, substraction, multiplication, exponentiation and division")
	print("Python Version 3.5")
	print("Developper: Larry Georges Muala")
	
	messagebox.showinfo("App Info", "App Name: Simple Python Calculator GUI\n" + 
						"\nApp description: Calculator GUI doing addition, substraction, multiplication, exponentiation and division\n" + 
						"\nPython Version 3.5 \n" + 
						"\nDevelopper: Larry Georges Muala")
#Menu design
menubar = tkinter.Menu(window)
myMenu = tkinter.Menu(menubar, tearoff=0)
myMenu.add_command(label="About", command=about_app)
myMenu.add_separator()
myMenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="App Info", menu=myMenu)

#Display menu
window.config(menu=menubar)


#CALCULATOR TEMPLATE SINGLE BUTTONS
screen_val = "0"

answer = "0"

#Calculator label window
lbl = tkinter.Label(window, text=screen_val, bg="gray", width=20)
lbl.grid(row=5, column=8)

#Blank label to create spaces
lbl_blank = tkinter.Label(window, text=" ", bg="gray2", font=("Helvetica", 1), width=20)
lbl_blank.grid(row=6, column=8)

#Calculator result label
lbl_answer = tkinter.Label(window, text=answer, bg="gray", width=20)
lbl_answer.grid(row=7, column=8)


#Button1 and function
def button1():
	global screen_val
	
	screen_val = lbl.cget("text")
	
	if screen_val == "0":
		lbl.configure(text="1")
	else:
		lbl.configure(text= screen_val + "1")
	
	
btn1 = tkinter.Button(window, text="1", font=("Helvetica", 10), height = 1, width = 5, command=button1)
btn1.grid(row=5, column=1)


#Button2 and function
def button2():
	global screen_val
	
	screen_val = lbl.cget("text")
	
	if screen_val == "0":
		lbl.configure(text="2")
	else:
		lbl.configure(text= screen_val + "2")
		
btn2 = tkinter.Button(window, text="2", font=("Helvetica", 10), height = 1, width = 5, command=button2)
btn2.grid(row=5, column=2)


#Button3 and function
def button3():
	global screen_val
	
	screen_val = lbl.cget("text")
	
	if screen_val == "0":
		lbl.configure(text="3")
	else:
		lbl.configure(text= screen_val + "3")
		
btn3 = tkinter.Button(window, text="3", font=("Helvetica", 10), height = 1, width = 5, command=button3)
btn3.grid(row=5, column=3)


#Button4 and function
def button4():
	global screen_val
	
	screen_val = lbl.cget("text")
	
	if screen_val == "0":
		lbl.configure(text="4")
	else:
		lbl.configure(text= screen_val + "4")
		
btn4 = tkinter.Button(window, text="4", font=("Helvetica", 10), height = 1, width = 5, command=button4)
btn4.grid(row=6, column=1)


#Button5 and function
def button5():
	global screen_val
	
	screen_val = lbl.cget("text")
	
	if screen_val == "0":
		lbl.configure(text="5")
	else:
		lbl.configure(text= screen_val + "5")
		
btn5 = tkinter.Button(window, text="5", font=("Helvetica", 10), height = 1, width = 5, command=button5)
btn5.grid(row=6, column=2)


#Button6 and function
def button6():
	global screen_val
	
	screen_val = lbl.cget("text")
	
	if screen_val == "0":
		lbl.configure(text="6")
	else:
		lbl.configure(text= screen_val + "6")
		
btn6 = tkinter.Button(window, text="6", font=("Helvetica", 10), height = 1, width = 5, command=button6)
btn6.grid(row=6, column=3)


#Button7 and function
def button7():
	global screen_val
	
	screen_val = lbl.cget("text")
	
	if screen_val == "0":
		lbl.configure(text="7")
	else:
		lbl.configure(text= screen_val + "7")
		
btn7 = tkinter.Button(window, text="7", font=("Helvetica", 10), height = 1, width = 5, command=button7)
btn7.grid(row=7, column=1)


#Button8 and function
def button8():
	global screen_val
	
	screen_val = lbl.cget("text")
	
	if screen_val == "0":
		lbl.configure(text="8")
	else:
		lbl.configure(text= screen_val + "8")
		
btn8 = tkinter.Button(window, text="8", font=("Helvetica", 10), height = 1, width = 5, command=button8)
btn8.grid(row=7, column=2)


#Button9 and function
def button9():
	global screen_val
	
	screen_val = lbl.cget("text")
	
	if screen_val == "0":
		lbl.configure(text="9")
	else:
		lbl.configure(text= screen_val + "9")
		
btn9 = tkinter.Button(window, text="9", font=("Helvetica", 10), height = 1, width = 5, command=button9)
btn9.grid(row=7, column=3)


#Button0 and function
def button0():
	global screen_val
	
	screen_val = lbl.cget("text")
	lbl.configure(text= screen_val + "0")
	
btn0 = tkinter.Button(window, text="0", font=("Helvetica", 10), height = 1, width = 5, command=button0)
btn0.grid(row=8, column=2)


#Dot Button and function
def Dot():
	global screen_val
	
	screen_val = lbl.cget("text")

	if "." in screen_val:
		print (True)
	else:
		lbl.configure(text= screen_val + ".")
		
btnDot = tkinter.Button(window, text=".", font=("Helvetica", 10), height = 1, width = 5, command=Dot)
btnDot.grid(row=8, column=3)


#Equal Button and function
def Equal():
	global screen_val
	
	screen_val = lbl.cget("text")
	
	print(screen_val)
	print("*************************")
	print(eval(screen_val))
	
	answer = eval(screen_val)
	lbl_answer.configure(text=str(answer))

	lbl.configure(text="0")
	
btnEqual = tkinter.Button(window, text="=", font=("Helvetica", 10), height = 1, width = 5, command=Equal)
btnEqual.grid(row=8, column=5)


#Exponent Button and function
def exponential():
	global screen_val
	
	screen_val = lbl.cget("text")
	lbl.configure(text= screen_val + "**")
	
btnExp = tkinter.Button(window, text="pow", font=("Helvetica", 10), height = 1, width = 5, command=exponential)
btnExp.grid(row=8, column=6)


#Division Button and function
def division():
	global screen_val
	
	screen_val = lbl.cget("text")
	lbl.configure(text= screen_val + "/")
	
btnDiv = tkinter.Button(window, text="÷", font=("Helvetica", 10), height = 1, width = 5, command=division)
btnDiv.grid(row=7, column=6)


#Multiplication Button and function
def multiplication():
	global screen_val
	
	screen_val = lbl.cget("text")
	lbl.configure(text= screen_val + "*")
	
btnMul = tkinter.Button(window, text="x", font=("Helvetica", 10), height = 1, width = 5, command=multiplication)
btnMul.grid(row=7, column=5)


#Substraction Button and function
def substraction():
	global screen_val
	
	screen_val = lbl.cget("text")
	lbl.configure(text= screen_val + "-")
	
btnMin = tkinter.Button(window, text="-", font=("Helvetica", 10), height = 1, width = 5, command=substraction)
btnMin.grid(row=6, column=6)


#Addition Button and function
def addition():
	global screen_val
	
	screen_val = lbl.cget("text")
	lbl.configure(text= screen_val + "+")
	
btnPlus = tkinter.Button(window, text="+", font=("Helvetica", 10), height = 1, width = 5, command=addition)
btnPlus.grid(row=6, column=5)


#Delete Button and function
def del_function():
	global screen_val
	
	screen_val = lbl.cget("text")
	length = len(screen_val)
	screen_val = screen_val[:length-1]
	lbl.configure(text=screen_val)
	
btnDel = tkinter.Button(window, text="←", font=("Helvetica", 10), height = 1, width = 5, command=del_function)
btnDel.grid(row=5, column=5)


#Clear Button and function
def Clr():
	global screen_val
	global answer
	
	answer = "0"
	screen_val = "0"
	lbl.configure(text=screen_val)
	lbl_answer.configure(text=answer)
	
btnClr = tkinter.Button(window, text="Clear", font=("Helvetica", 10), height = 1, width = 5, command=Clr)
btnClr.grid(row=5, column=6)


#Blank labels for separators between buttons and Calculation - Answer labels
lbl_blank = tkinter.Label(window, text=" ", bg="gray2")
lbl_blank.grid(row=5, column=4)

lbl_blank = tkinter.Label(window, text=" ", bg="gray2")
lbl_blank.grid(row=6, column=4)

lbl_blank = tkinter.Label(window, text=" ", bg="gray2")
lbl_blank.grid(row=7, column=4)

lbl_blank = tkinter.Label(window, text=" ", bg="gray2")
lbl_blank.grid(row=5, column=7)

lbl_blank = tkinter.Label(window, text=" ", bg="gray2")
lbl_blank.grid(row=6, column=7)

lbl_blank = tkinter.Label(window, text=" ", bg="gray2")
lbl_blank.grid(row=7, column=7)
##

window.mainloop()
