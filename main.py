# main.py
from cargar import cargar_archivo  # Importar la función cargar_archivo desde cargar.py
from calcular_tiempo import calcular_tiempo_ensamblaje


def main():
    opcion = 0
    lista_maquinas = None  # Inicializar la variable para almacenar las máquinas cargadas

    while opcion != 5:
        print("Menu Principal")
        print("1. Cargar Archivo")
        print("2. Procesar Archivo")
        print("3. Escribir Archivo de Salida")
        print("4. Calcular tiempo de ensamblaje")
        print("5. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("ERROR: No ingresó un número entero")
            print(" ")
            continue

        match opcion:
            case 1:
                ruta = input("Ingrese la ruta del archivo XML: ")
                # Acumular las máquinas cargadas
                lista_maquinas = cargar_archivo(ruta, lista_maquinas)
            case 2:
                if lista_maquinas:
                    lista_maquinas.imprimir()  # Asumiendo que Lista_Maquinas tiene un método imprimir implementado
                else:
                    print("ERROR: No hay máquinas cargadas. Cargue un archivo primero.")
            case 3:
                # Aquí puedes implementar la lógica para escribir el archivo de salida
                print("Escribir Archivo de Salida")

            case 4:
                if lista_maquinas:
                    print("Seleccione una máquina:")
                    actual_maquina = lista_maquinas.primero
                    index = 1
                    
                    # Mostrar las máquinas disponibles
                    while actual_maquina:
                        print(f"{index}. {actual_maquina.maquina.nombre}")
                        actual_maquina = actual_maquina.siguiente
                        index += 1
                    
                    seleccion = int(input("Ingrese el número de la máquina: "))
                    
                    # Volver a la cabeza de la lista enlazada de máquinas
                    actual_maquina = lista_maquinas.primero
                    contador = 1
                    
                    # Encontrar la máquina seleccionada
                    while actual_maquina and contador < seleccion:
                        actual_maquina = actual_maquina.siguiente
                        contador += 1
                    
                    if actual_maquina:
                        calcular_tiempo_ensamblaje(actual_maquina.maquina)
                    else:
                        print("ERROR: Máquina no encontrada.")
                else:
                    print("ERROR: No hay máquinas cargadas. Cargue un archivo primero.")

            case _:
                print("ERROR: Opción no válida")
                print(" ")

if __name__ == "__main__":
    main()
