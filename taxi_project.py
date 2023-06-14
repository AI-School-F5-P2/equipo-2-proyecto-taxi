# importe el módulo de tiempo para calcular la duración del viaje en taxi en segundos.
import time

# Registrar la hora de inicio de la carrera.
start_time = time.time()

# Constantes para tarifas
stop_tarifa = 0.02
move_tarifa = 0.05

# Calcula la duración del viaje en segundos
def calcular_tarifa(start_time, stop_time, si_moeve):
    duracion = stop_time - start_time

# Calcule la tarifa en función de si el taxi se mueve o no
    if si_moeve:
        tarifa = duracion * move_tarifa
    else:
        tarifa = duracion * stop_tarifa
    return tarifa

def start_program():
    print("Bienvenido al Programa de Cálculo de Tarifas de Taxi!")
    print("Este programa calcula la tarifa de un viaje en taxi según los criterios dados.")

    while True:
        print("\nPara comenzar la carrera, presiona Enter.")
        input("Presione Enter para comenzar...")

        # Inicializar el estado del taxi como detenido (sin movimiento)
        si_moeve = False

        print("\nInstrucciones:")
        print("Ingrese 's' si el taxi se está moviendo actualmente.")
        print("Ingrese 'p' si el taxi está detenido actualmente.")
        print("Presiona Enter para terminar la carrera y calcular la tarifa.")

        while True:
            status = input("Taxi estado: ").lower()
            if status == "s":
                si_moeve = True
            elif status == "p":
                si_moeve = False
            elif status == "":
                break
            else:
                print("Entrada inválida. Ingrese 's', 'p', o presione Enter.")

        # Registrar la hora de finalización de la carrera.
        stop_time = time.time()

        # Calcular la tarifa del viaje
        tarifa = calcular_tarifa(start_time, stop_time, si_moeve)

        # Mostrar la tarifa calculada
        print("Tarifa total: {:.2f} Euros".format(tarifa))

        # Solicitar al usuario que comience una nueva carrera o salga
        nueva_carrera = input("Empezar una nueva carrera? (yes/no): ").lower()
        if nueva_carrera != "y":
            break

# Program start
start_program()

