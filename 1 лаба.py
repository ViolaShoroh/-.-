from tkinter import *
root = Tk()
root.geometry('350x350')
root.title('350x350')
l1=Label(root, text = "Ширина", font="Arial 16",
         width=7, height=1)
l1.place(x = 10, y = 50)
e1=Entry(root, width=20)
e1.place(x = 120, y = 55) 
l2=Label(root, text = "Высота", font="Arial 16",
         width=7, height=1)
l2.place(x = 10, y = 100)
e2=Entry(root, width=20)
e2.place(x = 120, y = 105)

a = 350  #ширина - начальное значение
b = 350  #высота - начальное значение
def edit():
    global a, b
    w = e1.get() #ширина - изменение на
    h = e2.get() #высота - изменение на

    aa = len(w)
    bb = len(h)


    if w.isdigit():
        a = a + aa
    if w.isalpha():
        a = a - aa
    if h.isdigit():
        b = b + bb
    if h.isalpha():
        b = b - bb

    e1.delete(0, END)
    e2.delete(0, END)
    
    root.geometry('{}x{}'.format(a, b))
    razmer = str(a) + 'x' + str(b)
    root.title(razmer)
   
    
exit_button = Button(root, text="Закрыть", font="Arial 15",
                     bg="red", fg="white", command=root.destroy)
exit_button.place(x = 250, y = 150)

edit_button = Button(root, text="Изменить", font="Arial 15",
                     bg="green", command=edit)
edit_button.place(x = 10, y = 150)
root.mainloop()
