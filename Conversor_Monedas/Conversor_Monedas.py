from tkinter import *
from tkinter.messagebox import *


def convertir():
    try:
        euros = float(txteuros.get())
        
        dolares = round(euros*1.17,2)
        libras = round(euros*0.9,2)

        txtdolares.config(state='normal')
        txtdolares.delete(0,END)
        txtdolares.insert(0,dolares)
        txtdolares.config(state='disabled')
        
        txtlibras.config(state='normal')
        txtlibras.delete(0,END)
        txtlibras.insert(0,libras)
        txtlibras.config(state='disabled')


    except:
        
        print('Imposible to convert')
        showerror(message='Cannot convert',title='ERROR')




ventana = Tk(className='Conversor De Monedas')
ventana.geometry('500x200')


lbltitulo = Label(ventana,text='Conversor de Monedas')
lbltitulo.place(x=80,y=10,in_=ventana)
lbltitulo.config(font=("Courier",22))

lbleuros = Label(ventana,text='Euros')
lbleuros.place(x=70,y=80,in_=ventana)

txteuros = Entry(ventana,width=10)
txteuros.place(x=60,y=100,in_=ventana)


lbldolares = Label(ventana,text='Dolares')
lbldolares.place(x=350,y=60,in_=ventana)

txtdolares = Entry(ventana,width=10)
txtdolares.place(x=340,y=80,in_=ventana)
txtdolares.config(state='disabled')


lbllibras = Label(ventana,text='Libras')
lbllibras.place(x=350,y=100,in_=ventana)


txtlibras = Entry(ventana,width=10)
txtlibras.place(x=340,y=120,in_=ventana)
txtlibras.config(state='disabled')

btnconvertir = Button(ventana,text='Convertir',command=convertir,bg='blue')
btnconvertir.place(x=180,y=95,in_=ventana)

ventana.mainloop()