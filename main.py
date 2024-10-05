# main.py
from cargar import cargar_archivo, lista_maquinas_acumuladas, lista_productos_acumulados  # Importar las listas acumuladas
from calcular_tiempo import calcular_tiempo_ensamblaje
from grafico import generar_grafico

def main():
    opcion = 0  # Opciones del menú

    while opcion != 6:  # Cambiar a 6 para incluir la nueva opción
        print("Menu Principal")
        print("1. Cargar Archivo")
        print("2. Procesar Archivo")
        print("3. Calcular Tiempo de Ensamblaje")
        print("4. Generar Gráfico de Elaboración")
        print("5. Ver Productos Acumulados")
        print("6. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("ERROR: No ingresó un número entero")
            print(" ")
            continue

        match opcion:
            case 1:
                ruta = input("Ingrese la ruta del archivo XML: ")
                cargar_archivo(ruta)  # Cargar el archivo usando la función en cargar.py
            case 2:
                if lista_maquinas_acumuladas.primero:
                    lista_maquinas_acumuladas.imprimir()  # Imprimir todas las máquinas acumuladas
                else:
                    print("ERROR: No hay máquinas cargadas. Cargue un archivo primero.")
            case 3:
                if lista_maquinas_acumuladas.primero:
                    print("Seleccione una máquina:")
                    actual_maquina = lista_maquinas_acumuladas.primero
                    index = 1
                    
                    # Mostrar las máquinas disponibles
                    while actual_maquina:
                        print(f"{index}. {actual_maquina.maquina.nombre}")
                        actual_maquina = actual_maquina.siguiente
                        index += 1
                    
                    try:
                        seleccion = int(input("Ingrese el número de la máquina: "))
                    except ValueError:
                        print("ERROR: Debe ingresar un número entero.")
                        continue
                    
                    # Volver a la cabeza de la lista enlazada de máquinas
                    actual_maquina = lista_maquinas_acumuladas.primero
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
            case 4:
                pass  # Implementar la generación de gráfico de elaboración
            case 5:
                # Ver productos acumulados
                lista_productos_acumulados.imprimir()
            case 6:
                print("Saliendo del programa...")
            case _:
                print("ERROR: Opción no válida")
                print(" ")

if __name__ == "__main__":
    main()
