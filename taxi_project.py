# importe el módulo de tiempo para calcular la duración del viaje en taxi en segundos.
import asyncio
import time
import logging



# Configura el manejador de logs
logging.basicConfig(filename='registro.log', level=logging.DEBUG)

# Registrar la hora de inicio de la carrera.
logging.info('Inicio de carrera: {}'.format(time.ctime()))

start_time = time.time()


# Inicializar tarifas con POO
class TaxiTarifaCalculador:
    def __init__(self, stop_tarifa=0.02, move_tarifa=0.05):
        self.stop_tarifa = stop_tarifa
        self.move_tarifa = move_tarifa
        self.historial_carreras = []

    # Calcula la duración del viaje en segundos
    async def calcular_tarifa(self, start_time, stop_time, si_moeve):
        duracion = stop_time - start_time

        # Calcule la tarifa en función de si el taxi se mueve o no
        if si_moeve:
            tarifa = duracion * self.move_tarifa
        else:
            tarifa = duracion * self.stop_tarifa

            # crear diccionario con los datos de la carreas
        carrera = {'start_time': start_time, 'stop_time': stop_time, 'duracion': duracion, 'si_moeve': si_moeve,
                       'tarifa': tarifa}
        # agregar la carreas al historial
        self.historial_carreras.append(carrera)

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


    # start or the program
    async def start_program(self):
        logging.info("Iniciar programa")
        print("Bienvenido al Programa de Cálculo de Tarifas de Taxi!")
        print("Este programa calcula la tarifa de un viaje en taxi según los criterios dados.")

        while True:
            await asyncio.sleep(0.5)
            input("\nPresione Enter para comenzar...")
            logging.info("nuevo viaje")

            # Inicializar el estado del taxi como detenido (sin movimiento)
            si_moeve = False

            start_time = time.time()

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
                     self.restablecer_tarifa()
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

            #Guardar el historial de carreras en un archivo .txt
            with open('historial_carreras.txt', 'a') as archivo:
                for carrera in self.historial_carreras:
                    archivo.write('start Time: {}\n'. format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(carrera['start_time']))))
                    archivo.write('Stop Time: {}\n'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(carrera['stop_time']))))
                    archivo.write('Duración: {:.2f} seconds\n'.format(carrera['duracion']))
                    # archivo.write('Si se mueve: {}\n'.format(carrera['si_moeve']))
                    archivo.write("Stop Tarifa: {:.2f} Euros/segundos\n".format(self.stop_tarifa))
                    archivo.write("Move Tarifa: {:.2f} Euros/segundos\n".format(self.move_tarifa))
                    archivo.write('\nTarifa total: {:.2f} Euros\n\n'.format(carrera['tarifa']))



            # Solicitar al usuario que comience una nueva carrera o salga
            nueva_carrera = input("Empezar una nueva carrera? (yes/no): ").lower()
            if nueva_carrera != "y":

                print('\nHistorial de carreras guardado en el archivo historial_carreras.txt')
                break



calculator = TaxiTarifaCalculador()
asyncio.run(calculator.start_program())

print("--- %.5f seconds ---" % (time.time() - start_time))

logging.info("programa finalizada: {}" .format(time.ctime()))

