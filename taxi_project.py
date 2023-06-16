# importe el módulo de tiempo para calcular la duración del viaje en taxi en segundos.
import time
import unittest

# Registrar la hora de inicio de la carrera.
start_time = time.time()

# Constantes para tarifas
pordefecto_stop_tarifa = 0.02
pordefecto_move_tarifa = 0.05

# Inicializar tarifas
stop_tarifa = pordefecto_stop_tarifa
move_tarifa = pordefecto_move_tarifa


# Calcula la duración del viaje en segundos
def calcular_tarifa(start_time, stop_time, si_moeve, stop_tarifa, move_tarifa):
    duracion = stop_time - start_time


# Calcule la tarifa en función de si el taxi se mueve o no
    if si_moeve:
        tarifa = duracion * move_tarifa
    else:
        tarifa = duracion * stop_tarifa
    return tarifa


# Actualización de tarifas
def restablecer_tarifa():
    print('\nRestablecer tarifa? ')
    stop_tarifa = float(input('\nIntroduce la nueva tarifa parada (Euros por segundo): '))
    move_tarifa = float(input('Introduce la nueva tarifa movimiento (Euros por segundo): '))

    print('Tarifas actualizadas con éxito!')
    return stop_tarifa, move_tarifa


def start_program():
    print("Bienvenido al Programa de Cálculo de Tarifas de Taxi!")
    print("Este programa calcula la tarifa de un viaje en taxi según los criterios dados.")

    # Inicializar tarifas
    stop_tarifa = pordefecto_stop_tarifa
    move_tarifa = pordefecto_move_tarifa

    while True:
        input("\nPresione Enter para comenzar...")

        # Inicializar el estado del taxi como detenido (sin movimiento)
        si_moeve = False

        print("\nInstrucciones:")
        print("Ingrese 's' si el taxi se está moviendo actualmente.")
        print("Ingrese 'p' si el taxi está detenido actualmente.")
        print("Ingrese 'r' para restablecer las tarifas.")
        print("Presiona Enter para terminar la carrera y calcular la tarifa.")

        while True:
            status = input("Taxi estado: ").lower()
            if status == 's':
                si_moeve = True
            elif status == 'p':
                si_moeve = False
            elif status == '':
                break
            elif status == 'r':
                result = restablecer_tarifa()
                if result is not None:
                    stop_tarifa, move_tarifa = result

            else:
                print("Entrada inválida. Ingrese 's', 'p', 'r' o presione Enter.")

        # Registrar la hora de finalización de la carrera.
        stop_time = time.time()

        # Calcular la tarifa del viaje
        tarifa = calcular_tarifa(start_time, stop_time, si_moeve, stop_tarifa, move_tarifa)

        # Mostrar la tarifa calculada
        print("\nFare Calculation:")
        print("\nStart Time: {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))))
        print("End Time: {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stop_time))))
        print("Stopped Rate: {:.2f} Euros/second".format(stop_tarifa))
        print("Moving Rate: {:.2f} Euros/second".format(move_tarifa))
        print("Duration: {:.2f} seconds".format(stop_time - start_time))

        print("\nTarifa total: {:.2f} Euros".format(tarifa))

        # Solicitar al usuario que comience una nueva carrera o salga
        nueva_carrera = input("Empezar una nueva carrera? (yes/no): ").lower()
        if nueva_carrera != "y":
            break


start_program()


# unit test 1
class TarifaCalculacionTest(unittest.TestCase):
    def test_tarifa_calcula_stop(self):
        start_time = time.time()
        stop_time = start_time + 10
        si_moeve = False
        stop_tarifa = 0.02
        move_tarifa = 0.05

        tarifa_estimada = 10 * stop_tarifa

        tarifa = calcular_tarifa(start_time, stop_time, si_moeve, stop_tarifa, move_tarifa)

        self.assertEqual(tarifa_estimada, tarifa)

    def test_tarifa_calcula_move(self):
        start_time = time.time()
        stop_time = start_time + 10
        si_moeve = True
        stop_tarifa = 0.02
        move_tarifa = 0.05

        tarifa_estimada = 10 * move_tarifa

        tarifa = calcular_tarifa(start_time, stop_time, si_moeve, stop_tarifa, move_tarifa)

        self.assertEqual(tarifa_estimada, tarifa)


    if __name__ == '__main__':
        unittest.main()
