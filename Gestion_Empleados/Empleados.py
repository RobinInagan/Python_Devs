import os
import CRUD_EMPL

opt = 0

while(opt != 4):
    os.system('cls')
    print('\n|===============| Empelados |==============|\n')
    print('---> (1.) Inicializar DB')
    print('---> (2.) Insertar Empleado')
    print('---> (3.) Consultar Empleado')
    print('---> (4.) Salir\n')
    opt = int(input('\t ¿ Qué desea hacer ? ===>  '))
    if (opt==1):
        os.system('cls')
        CRUD_EMPL.init()
        os.system('pause')
    elif (opt==2):
        os.system('cls')

        print('\n|===============| Insertar Empelado |==============|\n')
        dni = int(input('Ingrese el DNI del empleado \t --> DNI = '))
        nombres = input('\nIngrese el nombre del empleado\t --> Nombre = ')
        apellidos = input('\nIngrese los apellidos del empleado\t --> Apellidos = ')
        edad = int(input('\nIngrese la edad del empleado\t --> Edad = '))
        departamento = input('\nIngrese el departamento del empleado\t --> Departamento = ')

        CRUD_EMPL.insert(dni, nombres, apellidos,edad,departamento)
        os.system('pause')
    elif (opt==3):
        os.system('cls')
        print('\n|===============| BUSCAR Empelado |==============|\n')
        dni = int(input('Ingrese el DNI del empleado \t --> DNI = '))     
        empleado = CRUD_EMPL.select_id(dni)

        if(len(empleado)!=0):
            print('\n¡ Empleado Encontrado ! \n\nMostrando Datos...\n')
            for x in empleado:
                print(f'{x[0]} {x[1]} {x[2]} {x[3]} {x[4]}\n')
        else:
            print('\n Empleado no encontrado, verifique la información \n')
        os.system('pause')
    elif (opt==4):
        os.system('cls')
        print('\nSaliendo del Programa...........\n')
        exit()

        
