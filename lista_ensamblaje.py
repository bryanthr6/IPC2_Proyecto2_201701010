class LineaEnsamblaje:
    def __init__(self, nombre, instrucciones):
        self.nombre = nombre
        self.instrucciones = [inst for inst in instrucciones if not inst.endswith("C0")]  # Filtramos C0
        self.posicion_actual = 0
        self.tiempo_total = 0
        self.tiempo_ensamblaje = 2  # Tiempo de ensamblaje
        self.tiempo_movimiento = 1   # Tiempo de movimiento
        self.ensamblando = False  # Estado de si está ensamblando
        self.tiempo_restante = 0  # Tiempo restante para terminar ensamblaje
    
    def mover_brazo(self):
        # Si está ensamblando, solo resta tiempo
        if self.ensamblando:
            self.tiempo_restante -= 1
            if self.tiempo_restante == 0:
                print(f"{self.nombre} terminó de ensamblar en {self.instrucciones[self.posicion_actual - 1]}")
                self.ensamblando = False
            return False
        
        # Si aún hay componentes por ensamblar
        if self.posicion_actual < len(self.instrucciones):
            if self.posicion_actual == 0:  # Movimiento a la primera posición
                print(f"{self.nombre} moviéndose a {self.instrucciones[self.posicion_actual]}")
                self.posicion_actual += 1
                return True  # Se movió a una nueva posición
            else:
                print(f"{self.nombre} moviéndose a {self.instrucciones[self.posicion_actual]}")
                self.posicion_actual += 1
                return True  # Se movió a una nueva posición
        
        return False  # Ya no se mueve más
    
    def ensamblar(self):
        # Si el brazo llega a una posición con componente, inicia el ensamblaje
        if not self.ensamblando and self.posicion_actual <= len(self.instrucciones):
            print(f"{self.nombre} ensamblando en {self.instrucciones[self.posicion_actual - 1]}")
            self.ensamblando = True
            self.tiempo_restante = self.tiempo_ensamblaje
            return True
        return False

    def esperando(self):
        # Mostrar que está esperando
        print(f"{self.nombre} esperando...")

def simular_ensamblaje(maquinas):
    tiempo_global = 0
    ensamblajes_completos = False
    
    while not ensamblajes_completos:
        ensamblajes_completos = True
        ensamblaje_realizado = False  # Indica si algún brazo está ensamblando en este ciclo

        # Primero, todos los brazos se mueven a su siguiente posición
        for maquina in maquinas:
            if maquina.mover_brazo():
                ensamblajes_completos = False  # Si se movió, hay más movimientos por hacer
            # Si llega a un componente ensamblable, lo ensamblamos
            if maquina.posicion_actual <= len(maquina.instrucciones):
                maquina.ensamblar()

        # Después, se procesan los ensamblajes
        for maquina in maquinas:
            if maquina.ensamblando:
                ensamblaje_realizado = True
                maquina.mover_brazo()  # Resta el tiempo de ensamblaje
        
        # Si hay un ensamblaje en curso, los demás esperan
        if ensamblaje_realizado:
            for maquina in maquinas:
                if not maquina.ensamblando and maquina.posicion_actual <= len(maquina.instrucciones):
                    maquina.esperando()

        tiempo_global += 1
        print(f"Tiempo actual: {tiempo_global}")

    return tiempo_global

# Ejemplo de uso con nuevas instrucciones
linea1 = LineaEnsamblaje("Línea 1", ["L1C2", "L1C6"])
linea2 = LineaEnsamblaje("Línea 2", ["L2C5"])

maquinas = [linea1, linea2]
tiempo_total = simular_ensamblaje(maquinas)
print(f"Tiempo total de ensamblaje: {tiempo_total}")
