import pymysql  

def select_Clientes():
    conexion = pymysql.connect(host="localhost",user="root",password="",database="proyecto_final")
    cursor = conexion.cursor()

    sql = "select * from cliente order by dni"
    cursor.execute(sql)
    clientes = cursor.fetchall()

    conexion.close()
    return clientes


def select_productos():
    conexion = pymysql.connect(host="localhost",user="root",password="",database="proyecto_final")
    cursor = conexion.cursor()

    sql = "select * from producto order by Nombre"
    cursor.execute(sql)
    productos = cursor.fetchall()

    conexion.close()
    return productos

def insert_pedido(idp,dni):

    conexion = pymysql.connect(host="localhost",user="root",password="",database="proyecto_final")
    cursor = conexion.cursor()

    sql = "Insert into pedido values('"+idp+"','"+dni+"')"
    cursor.execute(sql)
    conexion.commit()
    conexion.close()

def insert_lineas_pedido(idp,carrito):

    conexion = pymysql.connect(host="localhost",user="root",password="",database="proyecto_final")
    cursor = conexion.cursor()

    index = 1
    for x in carrito:
        sql = "insert into linea_pedido values('"+idp+"',"+str(index)+","+str(x[0])+","+str(x[3])+")"
        cursor.execute(sql)
        conexion.commit()
        
        index += 1
    conexion.close()  


