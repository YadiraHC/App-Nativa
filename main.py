from tkinter import*

root = Tk()
def promediar():
    resultado.set((cal1.get()+cal2.get()+cal3.get())/3)
    
    if resultado.get()<6:
        Label(root,text="Estas reprobado").pack()
    else:
        Label(root,text="Aprabado").pack()
cal1=IntVar()
cal2=IntVar()
cal3=IntVar()
resultado=IntVar()

text1 = Label(root,text="Escriba una calificacion").pack()
entrada1=Entry(root,textvariable=cal1).pack()

text2 = Label(root,text="Escriba una calificacion").pack()
entrada2=Entry(root,textvariable=cal2).pack()

text3 = Label(root,text="Escriba una calificacion").pack()
entrada3=Entry(root,textvariable=cal3).pack()

resultado = Label(root,text="Resultado").pack()
entradaR=Entry(root,textvariable=resultado).pack()

boton=Button(root,text="Promediar",command=promediar).pack()

root.mainloop