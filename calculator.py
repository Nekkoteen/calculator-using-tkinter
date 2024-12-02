from tkinter import *
import ast
i=0
def get_number(num):
  global i
  display.insert(i,num)
  i+=1
def get_operation(operator):
  global i
  length =len(operator)
  display.insert(i,operator)
  i+=length

def clear():
    display.delete(0,END)
    
def evaluate():
    equation = display.get()
    try:
        node = ast.parse(equation, mode='eval')
        result =eval(compile(node,'<string>','eval'))
        clear()
        display.insert(0,result)
    except :
        clear()
        display.insert(0,'Error')
        
def undo():
    equation = display.get()
    if len(equation)>0:
        new_equation = equation[:-1]
        clear()
        display.insert(0,new_equation)
        
root = Tk()

display = Entry(root)
display.grid(row=0, column=0, columnspan=6, padx=10, pady=10)  
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9',]
counter = 0
for x in range(3):  
    for y in range(3): 
        number_button = numbers[counter] 
        button = Button(root, text=number_button, width=5, height=2, command=lambda text=number_button : get_number(text))  
        button.grid(row=x+2, column=y)  
        counter += 1
        button = Button(root, text=0, width=5, height=2, command=lambda: get_number(0))  
        button.grid(row=5, column=1)  

operations = ['+', '-', '*', '/','*3.14',')','(','%','**','**2']
count=0
for x in range(4):
    for y in range(3):
        if count<len(operations):
            button = Button(root, text=operations[count], width=5, height=2, command=lambda text=operations[count] : get_operation(text))
            button.grid(row=x+2, column=y+3)
            count+=1

Button(root, text='AC', width=5, height=2, command=lambda:clear()).grid(row=5, column=0)       
Button(root, text='=', width=5, height=2, command=lambda:evaluate()).grid(row=5, column=2)  
Button(root, text='DEL', width=5, height=2, command=lambda:undo()).grid(row=5, column=4)  
     
root.mainloop()
