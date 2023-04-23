import os

opt = 0
Dict = {}
traducc = ''

while opt != 3 :
    os.system("cls")
    print('|==============| TRADUCTOR |============|\n')
    print('\n1. Insertar Palabra')
    print('\n2. Traducir Texto')
    print('\n3. Salir')

    try:
        opt = int(input('\nIngrese la opción que desea usar\n\t->'))
    except:
        os.system("cls")
        print('Error al leer la opción, finalizando programa....\n')
        exit()
    if(opt == 1):
        os.system("cls")
        print('|==============| INSERTAR |============|\n')
        esp = input('\n Ingrese una palabra en español\n--->  ')
        eng = input('\n Ingrese la traducción al inglés de la palabra {} \n--->  '.format(esp))
        Dict[esp] = eng
    if(opt==2):
        os.system("cls") 
        print('|==============| TRADUCIR |============|\n')
        espText = input('\n Ingrese el texto a traducir\n-: ')
        lista = espText.split()

        for x in lista:
            if(x in Dict):
                traducc = traducc + Dict[x] + ' '
            else:
                if(x != ' '):
                    traducc = traducc + 'X' + ' '
        
        print('\n|==============| TRADUCCION |============|\n')
        print(traducc)
        input('\n Enter para continuar.....')
        traducc = ''