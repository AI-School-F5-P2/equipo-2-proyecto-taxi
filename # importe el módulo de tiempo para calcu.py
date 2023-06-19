# importe el módulo de tiempo para calcular la duración del viaje en taxi en segundos.
import time
import unittest
import logging

logging.basicConfig(filename='registro.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Registrar la hora de inicio de la carrera.
logging.info('Inicio de carrera: {}'.format(time.ctime()))

# Constantes para tarifas
pordefecto_stop_tarifa = 0.02
pordefecto_move_tarifa = 0.05

# Inicializar tarifas
stop_tarifa = pordefecto_stop_tarifa
move_tarifa = pordefecto_move_tarifa

#lista para almacenar el historial de tarifas
historial_carreras =[]


# Calcula la duración del viaje en segundos
def calcular_tarifa(start_time, stop_time, si_moeve, stop_tarifa, move_tarifa):
    duracion = stop_time - start_time


# Calcule la tarifa en función de si el taxi se mueve o no
    if si_moeve:
        tarifa = duracion * move_tarifa
    else:
        tarifa = duracion * stop_tarifa
        #Añadir el resultado de la carrera al historial de tarifas
        historial_carreras.append((start_time, stop_time, stop_tarifa, move_tarifa, si_moeve,tarifa))       
    return tarifa

logging.basicConfig(filename='taxi.log',level=logging.INFO)

# Actualización de tarifas
def restablecer_tarifa():
    print('\nRestablecer tarifa?')
    stop_tarifa = float(input('\nIntroduce la nueva tarifa parada (Euros por segundo): '))
    move_tarifa = float(input('Introduce la nueva tarifa movimiento (Euros por segundo): '))

    print('Tarifas actualizadas con éxito!')
    mostrar_historial()

    return stop_tarifa, move_tarifa

def mostrar_historial():
    if historial_carreras:
        print("\nHistorial de carreras:")
    for i, carrera in enumerate(historial_carreras):
        print("Carrera{}: Tarifa total: {:2f} Euros".format(i+1, carrera[5]))
        print("Inicio: {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(carrera[0])))) 
        print("Fin: {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(carrera[1])))) 
        print("Tarifa de parada: {:.2f} Euros/segundo".format(carrera[2]))
        print("Tarifa de movimiento: {:.2f} Euros/segundo".format(carrera[3]))  
        print("Duración: {:.2f} segundos".format(carrera[1] - carrera[0])) 
        print("")
        if historial_carreras:
            print("\nHistorial de carreras:")
            for i, carrera in enumerate(historial_carreras):
                print("inicio: {}". format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(carrera[0]))))
                print("Fin: {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(carrera[1]))))
                print("Tarifa de parada: {:.2f} Euros/segundo".format(carrera[2]))
                print("Tarifa de movimiento: {:.2f} Euros/segundo".format(carrera[3]))
                print("Duración: {:.2f} segundos".format(carrera[5]))
                print("")
    else: 
        print("No hay registros de carreras pasadas.")


def start_program():
    print("Bienvenido al Programa de Cálculo de Tarifas de Taxi!")
    print("Este programa calcula la tarifa de un viaje en taxi según los criterios dados.")

# Inicializar tarifas
stop_tarifa = pordefecto_stop_tarifa
move_tarifa = pordefecto_move_tarifa

#registrar la hora de inicio de la carrera
logging.info('inicio de carrera: {}'.format(time.ctime()))


while True:
        input("\nPresione Enter para comenzar...")
 

# Registrar la hora de inicio de la carrera.
        start_time = time.time()

        # Inicializar el estado del taxi como detenido (sin movimiento)
        si_moeve = False


        print("\nInstrucciones:")
        print("Ingrese 's' si el taxi se está moviendo actualmente.")
        print("Ingrese 'p' si el taxi está detenido actualmente.")
        print("Ingrese 'r' para restablecer las tarifas.")
        print("Ingrese 'h' para solicitar todos los registros.")
        print("Presiona Enter para terminar la carrera y calcular la tarifa.")

        while True:
            accion = input("Ingrese la acción a realizar ('s'/'p'/'r'/'h'/'Enter'): ").lower()
            if accion == 's':
                si_moeve = True
            elif accion == 'p':
                si_moeve = False
            elif accion == '':
                break
            elif accion == 'r':
                result = restablecer_tarifa()
            elif accion == 'h':
                mostrar_historial()
            else:
                print("Entrada invalida.")


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
        logging.info('Duración: {:.2f} segundos; tarifa:{:.2f} Euros; Distancia recorrida:{} km; Estado del taxi: {}'.format)
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