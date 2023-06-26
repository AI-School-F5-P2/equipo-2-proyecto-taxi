# importe el módulo de tiempo para calcular la duración del viaje en taxi en segundos.
import asyncio
import time
import unittest
import logging
import os



if os.path.isfile('datos_tarifa'):
    print('Archivo creado correctamente' )
else:
    print('No se pudo crear el archivo')

# Configura el manejador de logs
logging.basicConfig(filename='taxi.log', level=logging.DEBUG)


<<<<<<< HEAD
# Registrar la hora de inicio de la carrera.
#logging.info('Inicio de carrera: {}'.format(time.ctime()))

# Inicializar tarifas con POO
class TaxiTarifaCalculador:
    def __init__(self, stop_tarifa=0.02, move_tarifa=0.05):
        self.stop_tarifa = stop_tarifa
        self.move_tarifa = move_tarifa
        self.historial_carreras = []

  
# Calcula la duración del viaje en segundos
    def calcular_tarifa(self, start_time, stop_time, si_moeve):
        duracion = stop_time - start_time
 
# crear diccionario con los datos de la carreas
        carrera = {'start_time': start_time, 'stop_time': stop_time, 'duracion': duracion, 'si_moeve': si_moeve,
                    'tarifa': 0}

# Calcule la tarifa en función de si el taxi se mueve o no
=======

start_time = time.time()


# Inicializar tarifas con POO
class TaxiTarifaCalculador:
    def __init__(self, stop_tarifa=0.02, move_tarifa=0.05):
        self.stop_tarifa = stop_tarifa
        self.move_tarifa = move_tarifa

    # Calcula la duración del viaje en segundos
    async def calcular_tarifa(self, start_time, stop_time, si_moeve):
        duracion = stop_time - start_time
        # Calcule la tarifa en función de si el taxi se mueve o no
>>>>>>> e6dca434fbb63c43fc0b2fc9296829bfead84bf6
        if si_moeve:
            tarifa = duracion * self.move_tarifa
        else:
            tarifa = duracion * self.stop_tarifa
<<<<<<< HEAD

        carrera['tarifa'] = tarifa

        #agregar la carreas al historial
        self.historial_carreras.append(carrera)   


        #Guardar los datos en un archivo .txt
        with open('datos_tarifa.txt', 'w') as archivo:
            archivo.write("Start Time: {}\n".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))))
            archivo.write("End Time: {}\n".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stop_time))))
            archivo.write("Stop Tarifa: {:.2f} Euros/segundos\n".format(self.stop_tarifa))
            archivo.write("Move Tarifa: {:.2f} Euros/segundos\n".format(self.move_tarifa))
            archivo.write("Duracion: {:.2f} seconds\n\n".format(stop_time - start_time))
            archivo.write("Tarifa total: {:.2f} Euros".format(tarifa))


        return tarifa
    

# Actualización de tarifas
    def restablecer_tarifa(self): 
        logging.info('\nRestablecer tarifa?')
        stop_tarifa = float(input('Introduce la nueva tarifa parada (Euros por segundo): '))
        move_tarifa = float(input('Introduce la nueva tarifa movimiento (Euros por segundo): '))

        self.stop_tarifa = stop_tarifa
        self.move_tarifa = move_tarifa


        logging.info("Tarifas actualizadas: stop tarifa: %s, move tarifa: %s", stop_tarifa, move_tarifa)
        print('Tarifas actualizadas con éxito!')

        

    def start_program(self):
        logging.info("Iniciar programa")
=======
        return tarifa

    # Actualización de tarifas
    async def restablecer_tarifa(self):
        print('\nRestablecer tarifa? ')
        stop_tarifa = float(input('Introduce la nueva tarifa parada (Euros por segundo): '))
        move_tarifa = float(input('Introduce la nueva tarifa movimiento (Euros por segundo): '))
        self.stop_tarifa = stop_tarifa
        self.move_tarifa = move_tarifa
        print('Tarifas actualizadas con éxito!')

    # start or the program
    async def start_program(self):
>>>>>>> e6dca434fbb63c43fc0b2fc9296829bfead84bf6
        print("Bienvenido al Programa de Cálculo de Tarifas de Taxi!")
        print("Este programa calcula la tarifa de un viaje en taxi según los criterios dados.")

        while True:
<<<<<<< HEAD
            input("\nPresione Enter para comenzar...")
            logging.info("nuevo viaje")

        # Inicializar el estado del taxi como detenido (sin movimiento)
            si_moeve = False
=======
            await asyncio.sleep(0.5)
            input("\nPresione Enter para comenzar...")

            # Inicializar el estado del taxi como detenido (sin movimiento)
            si_moeve = False

            # Registrar la hora de inicio de la carrera.
>>>>>>> e6dca434fbb63c43fc0b2fc9296829bfead84bf6
            start_time = time.time()

            print("\nInstrucciones:")
            print("Ingrese 's' si el taxi se está moviendo actualmente.")
            print("Ingrese 'p' si el taxi está detenido actualmente.")
            print("Ingrese 'r' para restablecer las tarifas.")
            print("Presiona Enter para terminar la carrera y calcular la tarifa.")
<<<<<<< HEAD

=======
>>>>>>> e6dca434fbb63c43fc0b2fc9296829bfead84bf6
            while True:
                status = input("Taxi estado: ").lower()
                if status == 's':
                    si_moeve = True
                elif status == 'p':
                    si_moeve = False
                elif status == '':
                    break
                elif status == 'r':
<<<<<<< HEAD
                    self.restablecer_tarifa()

                else:
                    print("Entrada inválida. Ingrese 's', 'p', 'r' o presione Enter.")

        # Registrar la hora de finalización de la carrera.
            stop_time = time.time()
        # Calcular la tarifa del viaje
            tarifa = self.calcular_tarifa(start_time, stop_time, si_moeve)

        # Mostrar la tarifa calculada
            print("\nCalculacion de Tarifa:")
            print("\nStart Time: {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))))
            print("End Time: {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stop_time))))
            print("Stop Tarifa: {:.2f} Euros/segundos".format(self.stop_tarifa))
            print("Move Tarifa: {:.2f} Euros/segundos".format(self.move_tarifa))
            print("Duracion: {:.2f} seconds".format(stop_time - start_time))
            print("\nTarifa total: {:.2f} Euros".format(tarifa))
            logging.info("\nTarifa total: {:.2f} Euros".format(tarifa))
                # Solicitar al usuario que comience una nueva carrera o salga
            nueva_carrera = input("Empezar una nueva carrera? (yes/no): ").lower()
            if nueva_carrera != "y":
                break 

            #Guardar el historial de carreras en un archivo .txt
            with open('historial_carreras.txt', 'w') as archivo:
                for carrera in self.historial_carreras:
                    archivo.write('start Time: {}\n'. format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(carrera['start_time']))))
                    archivo.write('Stop Time: {}\n'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(carrera['stop_time']))))
                    archivo.write('Duración: {:.2f} seconds\n'.format(carrera['duracion']))
                    archivo.write('Si se mueve: {}\n'.format(carrera['si_moeve']))
                    archivo.write('Tarifa total: {:.2f} Euros\n\n'.format(carrera['tarifa']))

                    print('\nHistorial de carreras guardado en el archivo historial_carreras.txt')
=======
                    await self.restablecer_tarifa()
                else:
                    print("Entrada inválida. Ingrese 's', 'p', 'r' o presione Enter.")

            # Registrar la hora de finalización de la carrera.
            stop_time = time.time()

            # Calcular la tarifa del viaje
            tarifa = await self.calcular_tarifa(start_time, stop_time, si_moeve)

            # Mostrar la tarifa calculada
            print("\nCalculacion de Tarifa:")
            print("\nStart Time: {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))))
            print("End Time: {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stop_time))))
            print("Stop Tarifa: {:.2f} Euros/segundos".format(self.stop_tarifa))
            print("Move Tarifa: {:.2f} Euros/segundos".format(self.move_tarifa))
            print("Duracion: {:.2f} seconds".format(stop_time - start_time))
            print("\nTarifa total: {:.2f} Euros".format(tarifa))

            # Solicitar al usuario que comience una nueva carrera o salga
            nueva_carrera = input("Empezar una nueva carrera? (yes/no): ").lower()
            if nueva_carrera != "y":
                break


async def main():
    calculator = TaxiTarifaCalculador()
    await calculator.start_program()


if __name__ == "__main__":
    asyncio.run(main())


print("--- %.5f seconds ---" % (time.time() - start_time))
>>>>>>> e6dca434fbb63c43fc0b2fc9296829bfead84bf6








        logging.info("programa finalizador")
calculator = TaxiTarifaCalculador()
calculator.start_program()



# unit test 1
class TarifaCalculacionTest(unittest.TestCase):
    def test_tarifa_calcula_stop(self):
        calculator = TaxiTarifaCalculador()
        tarifa = calculator.calcular_tarifa(0, 20, False)
        self.assertEqual(tarifa, 0.4)

    def test_tarifa_calcula_move(self):
        calculator = TaxiTarifaCalculador()
        tarifa = calculator.calcular_tarifa(0, 20, True)
        self.assertEqual(tarifa, 1)

    def test_tarifa_calcula_tarifaRestablesida(self):
        calculator = TaxiTarifaCalculador(0.3, 0.7)
        tarifa = calculator.calcular_tarifa(0, 20, True)
        self.assertEqual(tarifa, 14)


if __name__ == '__main__':

    unittest.main()