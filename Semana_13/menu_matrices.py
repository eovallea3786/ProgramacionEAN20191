import json
from Semana_10.menu import ingresar_vector
diccionario = {}
matrices = {}

def leer_matriz():
    """
    Lee una matriz por teclado
    :return: (list of list of int) la matriz del usuario
    """
    resultado = []
    while True:
        entrada = input('Desea ingresar una fila? s/n ')
        if entrada == 'n':
            break
        resultado.append(ingresar_vector()[1:])
    return resultado

def guardar(nombre_archivo, diccionario_a_guardar):
    """
    (str,dict) -> Boolean

    Guarda en el archivo mencionadoel diccionario

    :param nombre_archivo:
    :param diccionario_a_guardar:
    :return:
    """

    try:
        # Abrimos nuestro archivo
        archivo= open(nombre_archivo,"w")

        #convertimos nuestro diccionario en un archivo .json
        convertido= json.dumps(diccionario_a_guardar)

        # guardamos el archivo
        archivo.write(convertido)

        #Cerramos el archivo
        archivo.close()

        return True
    except:

        #si ocurre algun error retorna falso
        return False

def leer_(nombre_archivo):

    """
    (str) -> dict
    :param nombre_archivo:
    :return:
    """

    try:
        archivo=open(nombre_archivo,"r")
        diccionario_leido = json.load(archivo)
        archivo.close()
        return diccionario_leido

    except:
        return ()

def principal():
    while True:

        MENU = """
        **********Menu**********
        0. Salir
        1. Ingresar Matriz
        2. Ver Matrices
        ************************
        """

        seleccion = input(MENU)
        if seleccion == '0':
            print('Suerte')
            break
        elif seleccion == "1":
            nombre = input('cual es el nombre de su matriz ')
            matriz = leer_matriz()
            matrices[nombre] = matriz
        elif seleccion == "2":
            print('Sus matrices')
            for matriz in matrices:
                print(matriz, "=")
                print(matrices[matriz])
        else:
            print("Seleccion invalida")

if __name__ == "__main__":
    principal()
    nombre_archivo = "prueba.json"
    leido = leer_(nombre_archivo)
    print(leido)
    print(guardar(nombre_archivo, diccionario))
    if guardar(nombre_archivo, matrices):
        print("Sus matrices fueron guardadas con exito")
    else:
        print("NO fueron guardadas sus matrices")