from tkinter import*

def add() :
  str=eval(e1.get()+'+'+e2.get())
  l4.configure(text=str)

def sub() :
  str=eval(e1.get()+'-'+e2.get())
  l4.configure(text=str)

def mul() :
  str=eval(e1.get()+'*'+e2.get())
  l4.configure(text=str)

def div():
  str=eval(e1.get()+'/'+e2.get())
  l4.configure(text=str)

win=Tk()
f1=Frame()
f2=Frame()
win.geometry('500x500')

l1=Label(f1, text='Oprand 1')
l2=Label(f1, text='Oprand 2')
e1=Entry(f1)
e2=Entry(f1)
l3=Label(f1, text='Result')
l4=Label(f1, bg='red', text='', height=1, width=10)
btn1=Button(f2, text='+', command=add)
btn2=Button(f2, text='-', command=sub)
btn3=Button(f2, text='*', command=mul)
btn4=Button(f2, text='/', command=div)

l1.grid(column=0, row=0)
l2.grid(column=0, row=1)
e1.grid(column=1, row=0)
e2.grid(column=1, row=1)
l3.grid(column=2, row=0, columnspan=2, rowspan=2)
l4.grid(column=4, row=0, columnspan=2, rowspan=2)
btn1.grid(column=0, row=0)
btn2.grid(column=1, row=0)
btn3.grid(column=2, row=0)
btn4.grid(column=3, row=0)

f1.pack()
f2.pack()

win.mainloop()