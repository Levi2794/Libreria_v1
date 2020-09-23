#Importacion de la libreria peewee
from peewee import *
from collections import OrderedDict #Ordena los elemntos del diccionario

import sys

#Creacion de la base de datos
db = SqliteDatabase('libreria.db')

#Modelos de base de datos
class librerias(Model):
    id_libreria = AutoField()
    nom_libreria = CharField(50)
    pag_libreria = CharField(50)
    
    class Meta:
        database = db

class libros(Model):
    id_libro = AutoField()
    titulo_lib = CharField(50)
    autor_lib = CharField(50)
    genero_lib = CharField(50)
    editorial_lib = CharField(50)
    precio_lib = FloatField(8)
    cantidad_lib = DoubleField(3)
    descripcion_lib = TextField()
    
    class Meta:
        database = db

#class autor(Model):
    #id_autor = AutoField()
    #nom_autor = ForeignKeyField(libros, backref='libros')
    #naci_autor = CharField(20)
    #class Meta:
    #    database = db
        
class usuario(Model):
    id_usuario = AutoField()
    nom_usuario = CharField()
    
    class Meta:
        database = db
        
class administrador(Model):
    id_admin = AutoField()
    nom_admin = CharField()
    password = CharField(10)
    
    class Meta:
        database = db
        
#creacion y coneccion de base de datos y tabalas
def coneccion():
    db.connect()
    db.create_tables([librerias, libros, usuario, administrador], safe = True)

#menu principal
def principal():
    print('\nBienvenido a mi aplicación\n')
    
    choice = None
    while choice != 'S':
        for key,value in menu_p.items():    #Optenemos los items y los asignamos a sus variables correspondientes
            print('{}) {}'.format(key,value.__doc__))   #Accede a las funciones con __doc__
        print('Precione S para salir')
        choice = input('\nopc: ').upper().strip()
        if choice in menu_p:
            menu_p[choice]()
            break

def menu_usuario():
    '''Usuario'''
    print('\nBienvenido al menu de usuarios\n')
    
    choice = None
    while choice != 'S':
        for key,value in menu_us.items():    #Optenemos los items y los asignamos a sus variables correspondientes
            print('{}) {}'.format(key,value.__doc__))   #Accede a las funciones con __doc__
        print('Precione S para salir')
        choice = input('\nopc: ').upper().strip()
        if choice in menu_us:
            menu_us[choice]()
            break
        
def listar():
    '''Listar'''
    print('\nMenu')
    print('\n1) Librerias\n2) Libros\n3) Salir')
    
    try:
        opc = int(input('Opcion: '))
    except TypeError:
        print('\nOpcion incorrecta...')
        listar()
    else:
        if opc == 1:
            print('\nLista de Libreria')
            print('\n1) Todas\n2)Buscar libreria\n3)salir')
            try:
                opc_2 = int(input('Opcion: '))
            except TypeError:
                print('\nOpcion incorrecta...')
                listar()
            else:
                if opc_2 == 1:
                    print('\nTodas las Librerias\n')
                    for libreria in librerias.select():    #Devuelte los registros de la tabla librerias
                        print('Libreria: {}\nPagina Web: {}'.format(libreria.nom_libreria, libreria.pag_libreria))
                    menu_usuario()
                        
                elif opc_2 == 2:
                    print('\nBusca tu libreria\n')
                    nombre_l = input('Libreria: ')
                    librerias_n = librerias.get_or_none(librerias.nom_libreria == nombre_l)   #Buscamos el registro en las tablas
                    
                    if librerias_n != None:                   
                        print('\nLibreria: {}\nPagina Web: {}'.format(librerias_n.nom_libreria, librerias_n.pag_libreria))
                        menu_usuario()
                    else:
                        print('\nLa libreria que buscas no esta registrada....')
                        listar()
                    
                elif opc_2 == 3:
                    return 0
                else:
                    print('\nOpcion incorrecta....')
                    listar()
                    
        elif opc == 2:
            print('\nLista de Libros')
            print('\n1) Todas\n2)Buscar libro\n3)salir')
            try:
                opc_3 = int(input('Opcion: '))
            except TypeError:
                print('\nOpcion incorrecta...')
                listar()
            else:
                if opc_3 == 1:
                    print('\nTodas los Libros\n')
                    for libro in libros.select():    #Devuelte los registros de la tabla librerias
                        print('Titulo: {}\nAutor: {}\nGenero: {}\nEditorial: {}\nPrecio: {}\nDescripción: {}\nCantidad: {}'.format(libro.titulo_lib, 
                                                                                                                     libro.autor_lib, 
                                                                                                                     libro.genero_lib, 
                                                                                                                     libro.editorial_lib, 
                                                                                                                     libro.precio_lib,
                                                                                                                     libro.cantidad_lib,
                                                                                                                     libro.descripcion_lib))
                    menu_usuario()
                        
                elif opc_3 == 2:
                    print('\nBusca tu libro\n')
                    titulo_li = input('Libro: ')
                    libro_n = libros.get_or_none(libros.titulo_lib == titulo_li)   #Buscamos el registro en las tablas
                    
                    if libro_n != None:                   
                        print('Titulo: {}\nAutor: {}\nGenero: {}\nEditorial: {}\nPrecio: {}\nDescripción: {}\nCantidad: {}'.format(libro_n.titulo_lib, 
                                                                                                                     libro_n.autor_lib, 
                                                                                                                     libro_n.genero_lib, 
                                                                                                                     libro_n.editorial_lib, 
                                                                                                                     libro_n.precio_lib,
                                                                                                                     librerias_n.cantidad_lib,
                                                                                                                     libro_n.descripcion_lib))
                        menu_usuario()
                    else:
                        print('\nEl libro que buscas no esta registrado....')
                        listar()
                    
                elif opc_2 == 3:
                    exit()
                else:
                    print('\nOpcion incorrecta....')
                    listar()
            
        elif opc == 3:
            return 0
        else:
            print('\nOpcion incorrecta....')
            listar()

def comprar():
    '''Compara'''
    print('\nCompra')
    i = None
    lista_compra = list()
    lista_libros = list()
    n = 0
    while i != 'N':
        i = None
        compra = input('\nLibro: ')
        compra_l = libros.get_or_none(libros.titulo_lib == compra)
        
        if compra_l != None:
            print('\nTitulo: {}\nAutor: {}\nGenero: {}\nEditorial: {}\nPrecio: ${}\nDescripción: {}\nCantidad: {}'.format(compra_l.titulo_lib, 
                                                                                                                     compra_l.autor_lib, 
                                                                                                                     compra_l.genero_lib, 
                                                                                                                     compra_l.editorial_lib, 
                                                                                                                     compra_l.precio_lib,
                                                                                                                     compra_l.cantidad_lib,
                                                                                                                     compra_l.descripcion_lib))
            lista_libros.append([compra_l.titulo_lib,compra_l.precio_lib])
            lista_compra.append(compra_l.precio_lib)
            total = sum(lista_compra)
            
            while i != 'S' and i !='N':
                i = input('Seguir comprando? [s/n]: ').upper().strip()
                    
        else:
            print('\nEl libro no se encuentra registrado....')
            while i != 'S' and i !='N':
                i = input('\nDesea eguir comprando? [s/n]: ').upper().strip()
    
    print('\nCompra')
    print(lista_libros)
    for l in lista_libros:
        for c in l:
            print(c)
    else:
        print('Total: ${}'.format(total))
    
def menu_admin():
    print('\nBienvenido al menu del administrador\n')
    
    choice = None
    while choice != 'S':
        for key,value in menu_ad.items():    #Optenemos los items y los asignamos a sus variables correspondientes
            print('{}) {}'.format(key,value.__doc__))   #Accede a las funciones con __doc__
        print('Precione S para salir')
        choice = input('\nopc: ').upper().strip()
        if choice in menu_ad:
            menu_ad[choice]()
            break

###Consultas
def crear():
    '''Crear'''
    print('\nMenu')
    print('\n1) Librerias\n2) Libros\n3) Administradores\n4) Salir')
    
    try:
        opc = int(input('Opcion: '))
    except TypeError:
        print('\nOpcion incorrecta...')
        crear()
    else:
        if opc == 1:
            print('\nAgregar Libreria')
            nom_lib = input('\nLibreria: ')
            pag_lib = input('Pag web: ')
            
            libre = librerias(nom_libreria=nom_lib, pag_libreria=pag_lib)
            libre.save()
            
            if libre.get_or_none != None:
                print('\nAdministrador agregado con exito....')
                menu_admin()
            else:
                print('Error al agregar al Administrador....')
                crear()
            
        elif opc == 2:
            print('\nAgregar Libros')
            tit = input('Titulo: ')
            aut = input('Autor: ')
            gen = input('Genero: ')
            edi = input('Editorial: ')
            pre = float(input('Precio: '))
            cant = int(input('Cantidad: '))
            print('Descripción: ')
            des = sys.stdin.read().strip()
            
            libr = libros(titulo_lib=tit, autor_lib=aut, genero_lib=gen, editorial_lib=edi, precio_lib=pre,
                          cantidad_lib=cant, descripcion_lib=des)
            libr.save()
            
            if libr.get_or_none != None:
                print('\nLibro agregado con exito....')
                menu_admin()
            else:
                print('Error al agregar el Libro....')
                crear()
            
        elif opc == 3:
            print('\nAgregar Administrador')
            nom_ad = input('\nNombre: ')
            pass_ad = input('Contraseña: ')
            
            admi = administrador(nom_admin=nom_ad, password=pass_ad)
            admi.save()
            
            if admi.get_or_none != None:
                print('\nAdministrador agregado con exito....')
                menu_admin()
            else:
                print('Error al agregar al Administrador....')
                crear()
            
        elif opc == 4:
            return 0
        else:
            print('\nOpcion incorrecta....')
            crear()
    
def mostar():
    '''Listar'''
    print('\nMenu')
    print('\n1) Librerias\n2) Libros\n3) Administradores\n4) Salir')
    
    try:
        opc = int(input('Opcion: '))
    except TypeError:
        print('\nOpcion incorrecta...')
        mostar()
    else:
        if opc == 1:
            print('\nLista de Libreria')
            print('\n1) Todas\n2)Buscar libreria\n3)salir')
            try:
                opc_2 = int(input('Opcion: '))
            except TypeError:
                print('\nOpcion incorrecta...')
                mostar()
            else:
                if opc_2 == 1:
                    print('\nTodas las Librerias\n')
                    for libreria in librerias.select():    #Devuelte los registros de la tabla librerias
                        print('Libreria: {}\nPagina Web: {}'.format(libreria.nom_libreria, libreria.pag_libreria))
                    menu_admin()
                        
                elif opc_2 == 2:
                    print('\nBusca tu libreria\n')
                    nombre_l = input('Libreria: ')
                    librerias_n = librerias.get_or_none(librerias.nom_libreria == nombre_l)   #Buscamos el registro en las tablas
                    
                    if librerias_n != None:                   
                        print('\nLibreria: {}\nPagina Web: {}'.format(librerias_n.nom_libreria, librerias_n.pag_libreria))
                        menu_admin()
                    else:
                        print('\nLa libreria que buscas no esta registrada....')
                        mostar()
                    
                elif opc_2 == 3:
                    return 0
                else:
                    print('\nOpcion incorrecta....')
                    mostar()
                    
        elif opc == 2:
            print('\nLista de Libros')
            print('\n1) Todas\n2)Buscar libro\n3)salir')
            try:
                opc_3 = int(input('Opcion: '))
            except TypeError:
                print('\nOpcion incorrecta...')
                mostar()
            else:
                if opc_3 == 1:
                    print('\nTodas los Libros\n')
                    for libro in libros.select():    #Devuelte los registros de la tabla librerias
                        print('Titulo: {}\nAutor: {}\nGenero: {}\nEditorial: {}\nPrecio: {}\nDescripción: {}\nCantidad: {}'.format(libro.titulo_lib, 
                                                                                                                     libro.autor_lib, 
                                                                                                                     libro.genero_lib, 
                                                                                                                     libro.editorial_lib, 
                                                                                                                     libro.precio_lib,
                                                                                                                     libro.cantidad_lib,
                                                                                                                     libro.descripcion_lib))
                    menu_admin()
                        
                elif opc_3 == 2:
                    print('\nBusca tu libro\n')
                    titulo_li = input('Libro: ')
                    libro_n = libros.get_or_none(libros.titulo_lib == titulo_li)   #Buscamos el registro en las tablas
                    
                    if libro_n != None:                   
                        print('Titulo: {}\nAutor: {}\nGenero: {}\nEditorial: {}\nPrecio: {}\nDescripción: {}\nCantidad: {}'.format(libro_n.titulo_lib, 
                                                                                                                     libro_n.autor_lib, 
                                                                                                                     libro_n.genero_lib, 
                                                                                                                     libro_n.editorial_lib, 
                                                                                                                     libro_n.precio_lib,
                                                                                                                     librerias_n.cantidad_lib,
                                                                                                                     libro_n.descripcion_lib))
                        menu_admin()
                    else:
                        print('\nEl libro que buscas no esta registrado....')
                        mostar()
                    
                elif opc_2 == 3:
                    return 0
                else:
                    print('\nOpcion incorrecta....')
                    mostar()
            
        elif opc == 3:
            print('\nLista de Administradores')
            print('\n1) Listar\n2) Salir')
            try:
                opc_4 = int(input('Opcion: '))
            except TypeError:
                print('\nOpcion incorrecta...')
                mostar()
            else:
                if opc_4 == 1:
                    print('\nTodas las Librerias\n')
                    for admin in administrador.select():    #Devuelte los registros de la tabla librerias
                        print('Admin: {}\nPassword: {}\n'.format(admin.nom_admin, admin.password))
                    menu_admin()
                elif opc_4 == 2:
                    return 0
                else:
                    print('\nOpcion incorrecta....')
                    mostar()
            
        elif opc == 4:
            return 0
        else:
            print('\nOpcion incorrecta....')
            mostar()

def eliminar():
    '''Eliminar'''
    print('\nMenu')
    print('\n1) Librerias\n2) Libros\n3) Administradores\n4) Salir')
    
    try:
        opc = int(input('Opcion: '))
    except TypeError:
        print('\nOpcion incorrecta...')
        eliminar()
    else:
        if opc == 1:
            print('\nEliminar de Libreria')
            print('\n1) Todas\n2)Buscar libreria\n3)salir')
            try:
                opc_2 = int(input('Opcion: '))
            except TypeError:
                print('\nOpcion incorrecta...')
                mostar()
            else:
                if opc_2 == 1:
                    print('\nTodas las Librerias\n')
                    d_librerias = librerias.get_or_none()
                    if d_librerias == None:
                        print('\nNo hay librerias registradas....')
                        menu_admin()
                    elif d_librerias != None:
                        de_librerias = librerias.delete().execute()
                        print('\nTodas las librerias se eliminaron correctamente....')
                        menu_admin()
                        
                elif opc_2 == 2:
                    print('\nBusca tu libreria\n')
                    nombre_l = input('Libreria: ')
                    librerias_n = librerias.get_or_none(librerias.nom_libreria == nombre_l)   #Buscamos el registro en las tablas
                    
                    if librerias_n == None:
                        print('\nLa libreria no esta registrada....')
                        menu_admin()
                    if librerias_n != None:                   
                        de_librerias = librerias.delete().where(librerias_n.nom_libreria == nombre_l).execute()
                        print('\nLa libreria {} se ha eliminado correctamente....'.format(nombre_l))
                        menu_admin()
                    else:
                        print('\nLa libreria que buscas no esta registrada....')
                        mostar()
                    
                elif opc_2 == 3:
                    return 0
                else:
                    print('\nOpcion incorrecta....')
                    mostar()
                    
        elif opc == 2:
            print('\nLista de Libros')
            print('\n1) Todos\n2) Buscar libro\n3) Salir')
            try:
                opc_3 = int(input('Opcion: '))
            except TypeError:
                print('\nOpcion incorrecta...')
                mostar()
            else:
                if opc_3 == 1:
                    print('\nTodos los Libros\n')
                    d_libro = libros.get_or_none()
                    
                    if d_libro == None:
                        print('\nNo hay libros registrados....')
                        menu_admin()
                    elif d_libro != None:
                        de_libro = libros.delete().execute()
                        print('\nTodas las libros se eliminaron correctamente....')
                        menu_admin()
                        
                elif opc_3 == 2:
                    print('\nBusca tu libro\n')
                    titulo_li = input('Libro: ')
                    libros_n = libros.get_or_none(libros.titulo_lib == titulo_li)
                    
                    if libros_n == None:
                        print('\nEl libro no esta registrado....')
                        menu_admin()
                    if libros_n != None:                   
                        de_libros = libros.delete().where(libros_n.titulo_lib == titulo_li).execute()
                        print('\nEl libro {} se ha eliminado correctamente....'.format(titulo_li))
                        menu_admin()
                    else:
                        print('\nEl libro que buscas no esta registrado....')
                        mostar()
                    
                elif opc_2 == 3:
                    return 0
                else:
                    print('\nOpcion incorrecta....')
                    mostar()
            
        elif opc == 3:
            print('\nEliminar Administradores')
            print('\n1) Buscar\n2) Salir')
            try:
                opc_4 = int(input('Opcion: '))
            except TypeError:
                print('\nOpcion incorrecta...')
                mostar()
            else:
                if opc_4 == 1:
                    print('\nBuscar administrador\n')
                    admin_de = input('Administrador: ')
                    admin_n = administrador.get_or_none(administrador.nom_admin == admin_de)
                    
                    if admin_n == None:
                        print('\nEl administrador no esta registrado....')
                        menu_admin()
                    if admin_n != None:                   
                        admin_d = administrador.delete().where(admin_n.nom_admin == admin_de).execute()
                        print('\nEl admin {} se ha eliminado correctamente....'.format(admin_de))
                        menu_admin()
                    else:
                        print('\nEl admin que buscas no esta registrado....')
                        mostar()
                elif opc_4 == 2:
                    return 0
                else:
                    print('\nOpcion incorrecta....')
                    mostar()
            
        elif opc == 4:
            return 0
        else:
            print('\nOpcion incorrecta....')
            eliminar()

def actualizar():
    '''Actualizar'''
    
def login_admin():
    '''Administrador'''
    i = 0
    while i < 3:
        nom = input('Ingresa un usuario: ')
        pas = input('Ingresa una contraseña: ')
        
        admin_db = administrador.get_or_none(administrador.nom_admin == nom)    #si el modelo no coinside, devuelve un None
        if admin_db != None:    #Si la variable es diferente de None
                if nom == admin_db.nom_admin and pas == admin_db.password:
                    menu_admin()
                    break
        else:
            print('Usiario y contraseña incorrecto....')
            i = i + 1
    principal()
        
#Menus
menu_p= OrderedDict([
    ('U', menu_usuario),
    ('A', login_admin)
])  #Creacion de un diccionario ordenado, los valores son los nombres de los metodos

menu_ad= OrderedDict([
    ('C', crear),
    ('L', mostar),
    ('E', eliminar),
    ('A', actualizar)
])  #Creacion de un diccionario ordenado, los valores son los nombres de los metodos

menu_us= OrderedDict([
    ('L', listar),
    ('C', comprar)
])  #Creacion de un diccionario ordenado, los valores son los nombres de los metodos

if __name__ == "__main__":
    coneccion()
    principal()
        
