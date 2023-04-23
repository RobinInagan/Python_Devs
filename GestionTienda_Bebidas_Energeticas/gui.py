from tkinter import *
from tkinter.ttk import *
from controlador import *
from tkinter.messagebox import *


clientes = []
productos =[] 
carrito = []

def insert():
    cantidad = int(sbnumero.get())
    if twprod.focus() == "":
        showerror("Error","Selecciona algún producto")
    elif cantidad == 0:
        showerror("Error","Cantidad seleccionada no puede ser cero")
    else:
        index = int(twprod.focus().split("I")[1],16) - 1
        producto = productos[index]
        importe = round(cantidad*producto[2],2)
        añadir_linea(twcarrito, txtTotal,producto,cantidad, importe)
        sbnumero.delete(0,"end")
        sbnumero.insert(0,0)
        carrito.append([producto[0],producto[1],producto[2],cantidad])

def end():
    cliente = cmbCliente.get()
    if cliente == "":
        showerror("Error","Debe seleccionar un cliente")
    elif len(carrito) == 0:
        showerror("Error","Imposible realizar un pedido sin articulos")
    else:
        try:
            dni = cliente.split("-")[0]
            nombreC = cliente.split("-")[1]
            end_pedi(carrito,dni,nombreC)
            twcarrito.delete(*twcarrito.get_children())
            carrito.clear()
            showinfo("Aviso","El pedido ha sido realizado con exito")
        except:
            showerror("Error","Error al realizar el pedido")    

ventana = Tk(className="Proyecto")
ventana.title = "Proyecto Final"

ventana.geometry("800x500")
ventana.resizable(False,False)

lblcliente = Label(ventana,text="Cliente")
lblcliente.place(x=100,y=20,in_=ventana)

cmbCliente = Combobox(ventana,width=80,state="readonly")
cmbCliente.place(x=160,y=20,in_=ventana)
clientes = cargar_clientes(cmbCliente)

lblprod = Label(ventana,text="Productos")
lblprod.place(x=140,y=90,in_=ventana)

twprod = Treeview(ventana,height=15)
twprod["columns"] = ("#1")
twprod.column("#0",width=180)
twprod.column("#1",width=60)
twprod.heading("#0",text="Nombre")
twprod.heading("#1",text="Precio")
twprod.place(x=60,y=120,in_=ventana)
productos = cargar_productos(twprod)

sbnumero = Spinbox(ventana,from_=0, to=10,width=5)
sbnumero.place(x=330,y=200,in_=ventana)
sbnumero.insert(0,0)

btninsert = Button(ventana,text=">>",width=5,command=insert)
btninsert.place(x=330,y=250,in_=ventana)

lblcarr = Label(ventana,text="Carrito de la compra")
lblcarr.place(x=520,y=90,in_=ventana)

twcarrito = Treeview(ventana,height=15)
twcarrito["columns"] = ("#1","#2")
twcarrito.column("#0",width=200)
twcarrito.column("#1",width=60)
twcarrito.column("#2",width=80)
twcarrito.heading("#0",text="Nombre")
twcarrito.heading("#1",text="Cant")
twcarrito.heading("#2",text="Importe")
twcarrito.place(x=400,y=120,in_=ventana)

btnfinalizar = Button(ventana,text="Finalizar compra",width=20,command=end)
btnfinalizar.place(x=400,y=450,in_=ventana)

lblTotal = Label(ventana,text="Total")
lblTotal.place(x=600,y=450,in_=ventana)

txtTotal = Entry(ventana,width=10,justify=RIGHT)
txtTotal.place(x=650,y=450,in_=ventana)
txtTotal.insert(END,"0.0 e")
txtTotal.config(state="readonly") 




ventana.mainloop()