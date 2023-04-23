from datetime import datetime
from accesoBD import *
import uuid
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

w,h = letter

def cargar_clientes(cmb_clientes):
    lista_clientes = select_Clientes()

    lista_clientes_format = []
    for x in lista_clientes:
        lista_clientes_format.append(str(x[0])+"-"+x[1])
    
    cmb_clientes["values"] = tuple(lista_clientes_format)

    return lista_clientes

def cargar_productos(twproductos):
    lista_productos = select_productos()

    for x in lista_productos:
        twproductos.insert("","end",text=x[1],values=str(x[2])+"e")
    
    return lista_productos

def añadir_linea(twcarrito, txtTotal,producto,cantidad, importe):
    twcarrito.insert("","end",text=producto[1],values=(cantidad,str(importe)))
    total = round(float(txtTotal.get().split("e")[0])+importe,2)

    txtTotal.config(state="active")
    txtTotal.delete(0,"end")
    txtTotal.insert(0,str(total)+"e")
    txtTotal.config(state="readonly")

def  end_pedi(carrito,dni,nombreC):
    idp = str(uuid.uuid4())
    insert_pedido(idp,dni)
    insert_lineas_pedido(idp,carrito)
    imprimir_ticket(idp,carrito,nombreC)

def imprimir_ticket(idp,carrito,nombreC):



    pdf=canvas.Canvas(idp+".pdf",pagesize=letter)

    linea = h-100
    pdf.setFontSize(14)
    pdf.drawString(100,linea,"N° Pedido: "+idp)
    linea=linea-20
    pdf.drawString(100,linea,"Cliente: "+nombreC)
    linea=linea-20
    fecha=datetime.now()
    pdf.drawString(100,linea,"Fecha: "+fecha.strftime("%d/%m/%y %H:%M:%S"))
    linea=linea-50

    total=0

    for x in carrito:
        pdf.drawString(140,linea,str(x[3])+" x "+ x[1])
        importe = round(x[2]*x[3],2)
        pdf.drawString(400,linea,str(importe)+" e")
        linea-=20
        total += importe
    
    pdf.line(100,linea,450,linea)   
    linea-=50
    pdf.setFontSize(22)
    pdf.drawString(150,linea,"Total: "+str(round(total,2))+" e")
    pdf.save()


