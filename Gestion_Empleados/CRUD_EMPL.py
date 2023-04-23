import pymysql

def insert(dni,nombre,apellidos,edad,departamento):
    conexion = pymysql.Connection(host='localhost',user='root',password='',database='practica21')
    cursor = conexion.cursor()

    sql = "insert into empleados values ("+str(dni)+",'"+nombre+"','"+apellidos+"','"+str(edad)+"','"+departamento+"')"

    cursor.execute(sql)
    conexion.commit()
    conexion.close()

def update(dni,nombre,apellidos,edad,departamento):
    conexion = pymysql.Connection(host='localhost',user='root',password='',database='practica21')
    cursor = conexion.cursor()

    sql = "update empleados set nombre = '"+nombre+"', apellidos = '"+apellidos+"', edad = '"+str(edad)+"'departamento='"+departamento+"' where dni = "+str(dni)
    
    cursor.execute(sql)
    conexion.commit()
    conexion.close()


def delete(dni):
    conexion = pymysql.Connection(host='localhost',user='root',password='',database='practica21')
    cursor = conexion.cursor()

    sql = "delete from empleados where dni = "+str(dni)

    cursor.execute(sql)
    conexion.commit()
    conexion.close()

def select():
    conexion = pymysql.Connection(host='localhost',user='root',password='',database='practica21')
    cursor = conexion.cursor()

    sql = "select * from empleados"
    cursor.execute(sql)
    filas = cursor.fetchall()    
    conexion.close()

    return filas

def select_id(dni):
    conexion = pymysql.Connection(host='localhost',user='root',password='',database='practica21')
    cursor = conexion.cursor()

    sql = "select * from empleados where dni = "+str(dni)
    cursor.execute(sql)
    filas = cursor.fetchall()    
    conexion.close()

    return filas

def init():
    conexion = pymysql.Connection(host='localhost',user='root',password='')
    cursor = conexion.cursor()
    
    sql = "create database if not exists practica21"

    cursor.execute(sql)
    
    sql = "USE practica21"

    cursor.execute(sql)

    sql = "create table if not exists `empleados`(dni int not null primary key,`nombre` varchar(20) not null,`apellidos` varchar(20) not null,edad int not null,`departamento` varchar(20) not null)"

    cursor.execute(sql)
    conexion.close()