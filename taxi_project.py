# importe el módulo de tiempo para calcular la duración del viaje en taxi en segundos.
import asyncio
import time


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
        if si_moeve:
            tarifa = duracion * self.move_tarifa
        else:
            tarifa = duracion * self.stop_tarifa
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
        print("Bienvenido al Programa de Cálculo de Tarifas de Taxi!")
        print("Este programa calcula la tarifa de un viaje en taxi según los criterios dados.")

        while True:
            await asyncio.sleep(0.5)
            input("\nPresione Enter para comenzar...")

            # Inicializar el estado del taxi como detenido (sin movimiento)
            si_moeve = False

            # Registrar la hora de inicio de la carrera.
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

