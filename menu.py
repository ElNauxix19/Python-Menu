# Importamos las librerias necesarias
import os
import time

# Creamos la funcion para limpiar la consola
def clear():
    os.system("cls")

def funcion_uno():
    # Limpiamos la consola
    clear()
    # Creamos el JavaScript
    with open("script.js",'w') as script:
        script.writelines("const usersDB = [\n")
        script.writelines('    "admin1",\n')
        script.writelines('    "admin2"\n')
        script.writelines("]\n")
        script.writelines("const passDB = [\n")
        script.writelines('    "admin123",\n')
        script.writelines('    "admin456"\n')
        script.writelines("]\n")
        script.writelines("const namesDB = [\n")
        script.writelines('    "Administrador1",\n')
        script.writelines('    "Administrador2"\n')
        script.writelines("]\n")
        script.writelines("var nombre\n")
        script.writelines("function check(){\n")
        script.writelines("    var uI = document.getElementById('uInp').value;\n")
        script.writelines("    var pI = document.getElementById('pInp').value;\n")
        script.writelines("    if(uI === usersDB[0] && pI === passDB[0]){\n")
        script.writelines("        nombre = namesDB[0];\n")
        script.writelines("        alert(nombre);\n")
        script.writelines("        event.preventDefault();\n")
        script.writelines("    }else if(uI === usersDB[1] && pI === passDB[1]){\n")
        script.writelines("        nombre = namesDB[1];\n")
        script.writelines("        alert(nombre);\n")
        script.writelines("        event.preventDefault();\n")
        script.writelines("    }else{\n")
        script.writelines('        alert("Error Fatal");\n')
        script.writelines("        event.preventDefault();\n")
        script.writelines("    }\n")
        script.writelines("}\n")
        
    # Creamos el HTML
    with open("index.html",'w',encoding="UTF-8") as index:
        index.writelines('<meta charset="UTF-8">')
        index.writelines('<title>Inicio de sesión</title>')
        index.writelines('<script src="script.js"></script>\n')
        index.writelines('<form onsubmit="check()">\n')
        index.writelines('    <input id="uInp" type="text" /><br>\n')
        index.writelines('    <input id="pInp" type="password" /><br>\n')
        index.writelines('    <input type="submit" />\n')
        index.writelines('</form>')
    
    # Indicamos al usuario que se ha completado el proceso
    print("Creando archivos...")
    time.sleep(4)
    print("Operacion completada con exito, cerrando programa")
    time.sleep(2)
    # Cerramos el programa
    exit()
    
    
def funcion_dos():
    clear()
    print("Proximos Proyectos")
    # Esperamos dos segundos y volvemos al menu principal
    time.sleep(2)
    
def funcion_iniciar():
    clear()
    print("***MENU DE SELECCIÓN DE SCRIPTS JAVASCRIPT***")
    print("***--------------BY ELNAUXIX19------------***\n")
    print("1.-Base de datos local (un archivo)")
    print("2.-Proximamente")
    print("3.-Salir del programa")
    
    select = input("Selecciona una opción:")

    # Aqui decimos que queremos que pase cuando pulse 1
    if select == "1":
        clear()
        print(f"Has elegido: {select}")
        y_n = input("¿Estas seguro?(Y/N):")
        if y_n == "y" or y_n == "Y":
            funcion_uno()
        elif y_n == "n" or y_n == "N":
            funcion_iniciar()
            
    # Aqui cuando pulse 2
    if select == "2":
        clear()
        print(f"Has elegido: {select}")
        y_n = input("¿Estas seguro?(Y/N):")
        if y_n == "y" or y_n == "Y":
            funcion_dos()
        elif y_n == "n" or y_n == "N":
            funcion_iniciar()
            
    # Y aqui 3
    if select == "3":
        clear()
        print(f"Has elegido: {select}")
        y_n = input("¿Estas seguro?(Y/N):")
        if y_n == "y" or y_n == "Y":
            exit()
        elif y_n == "n" or y_n == "N":
            funcion_iniciar()
      
    # EasterEgg
    if select == "mike":
        clear()
        print("EASTER EGG DESCUBIERTO")
        time.sleep(4)
            
    # Y aqui que si pulsamos cualquier otra tecla, se vuelva a mostrar el menu
    if select != "1" or select != "2" or select != "3" or select != "mike":
        funcion_iniciar()
        


funcion_iniciar()