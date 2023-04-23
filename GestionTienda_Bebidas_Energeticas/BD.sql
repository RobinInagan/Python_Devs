create database proyecto_final

use proyecto_final

create table cliente(
dni varchar(10) not null primary key,
Nombre varchar(100) not null,
direccion varchar(255) not null,
telefono int(10)not null
)

create table producto(
id_prod smallint not null primary key,
Nombre varchar(100) not null,
Precio float not null
)

create table pedido(
id_pedido varchar(255) not null,
dni_cliente varchar(20) not null,
foreign key (dni_cliente) references cliente(dni) ,
primary key (id_pedido,dni_cliente)
)

create table linea_pedido(
id_pedido varchar(255) not null,
id_linea smallint not null,
id_producto smallint not null,
cantidad smallint,
foreign key (id_pedido) references pedido(id_pedido),
foreign key (id_producto) references producto(id_prod),
primary key (id_pedido,id_linea)
)

INSERT INTO cliente VALUES ("46993520N","Miguel Rodríguez García","Calle Veracruz 3, Madrid","605441123");
INSERT INTO cliente VALUES ("56152518L","Sara Álamo Ruiz","Calle Espronceda 21 1B, Getafe","612005018");
INSERT INTO cliente VALUES ("93400868F","Fernando Giner Ríos","Calle Venenciadores 6 Bajo, Fuenlabrada","646225881");
INSERT INTO cliente VALUES ("14302538B","Alejandra Palacios Sillera","Calle Cerro del Águila 42 3A, Madrid","620633671");

INSERT INTO producto VALUES(1,"Coca-Cola 33cl",0.45);
INSERT INTO producto VALUES(2,"Cerveza Mahou 1l",1.2);
INSERT INTO producto VALUES(3,"Aquarius 1l",1.25);
INSERT INTO producto VALUES(4,"Cerveza Cruzcampo 33cl",0.75);
INSERT INTO producto VALUES(5,"Cerveza Cruzcampo 1l",1.3);
INSERT INTO producto VALUES(6,"Coca-Cola 2l",1.75);
INSERT INTO producto VALUES(7,"Fanta Naranja 2l",1.6);
INSERT INTO producto VALUES(8,"Sprite 2l",1.75);
INSERT INTO producto VALUES(9,"Cerveza Heineken 1l",1.5);
INSERT INTO producto VALUES(10,"Fantal limón 2l",1.6);
INSERT INTO producto VALUES(11,"Agua Fontvella 1l",0.75);
INSERT INTO producto VALUES(12,"Agua Solán de Cabras 1l",0.9);

select * from linea_pedido