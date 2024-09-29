# main.py
from cargar import cargar_archivo  # Importar la función cargar_archivo desde cargar.py

def main():
    opcion = 0
    lista_maquinas = None  # Inicializar la variable para almacenar las máquinas cargadas

    while opcion != 4:
        print("Menu Principal")
        print("1. Cargar Archivo")
        print("2. Procesar Archivo")
        print("3. Escribir Archivo de Salida")
        print("4. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("ERROR: No ingresó un número entero")
            print(" ")
            continue

        match opcion:
            case 1:
                ruta = input("Ingrese la ruta del archivo XML: ")
                lista_maquinas = cargar_archivo(ruta)  # Cargar el archivo usando la función en cargar.py
            case 2:
                if lista_maquinas:
                    lista_maquinas.imprimir()  # Asumiendo que Lista_Maquinas tiene un método imprimir implementado
                else:
                    print("ERROR: No hay máquinas cargadas. Cargue un archivo primero.")
            case 3:
                # Aquí puedes implementar la lógica para escribir el archivo de salida
                print("Escribir Archivo de Salida")
            case 4:
                print("Saliendo...")
            case _:
                print("ERROR: Opción no válida")
                print(" ")

if __name__ == "__main__":
    main()
