from tkinter import*

def f() :
  str1=e1.get()+'='+'%d'%eval(e1.get())
  l3.configure(text=str1)

win=Tk()
f1=Frame()
f2=Frame()
f3=Frame()
win.geometry('500x500')

l1=Label(f1, text='Operation')
e1=Entry(f1)
l2=Label(f2, text='Result')
l3=Label(f2, text='', height=1, width=20)
btn1=Button(f3, text='Calculating', command=f)

l1.grid(column=0, row=0)
e1.grid(column=1, row=0)
l2.grid(column=0, row=0)
l3.grid(column=1, row=0)
btn1.grid(column=1, row=0)

f1.pack()
f2.pack()
f3.pack()

win.mainloop()