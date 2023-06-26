# importe el módulo de tiempo y de tests
import unittest
import time
import asyncio

# para importar class TaxiTarifaCalculador de archivo principal
from taxi_project import TaxiTarifaCalculador


#  unit test 1
class TarifaCalculacionStopTest(unittest.TestCase):
    def test_tarifa_calcula_stop(self):
        calculator = TaxiTarifaCalculador()
        start_time = time.time()
        stop_time = start_time + 10
        si_moeve = False
        tarifa_esperada = 0.2

        # Call to the tarifa calculation
        tarifa_actual = asyncio.run(calculator.calcular_tarifa(start_time, stop_time, si_moeve))

       # Checking if expectada equal to calculated
        self.assertAlmostEqual(tarifa_actual, tarifa_esperada, places=2)

    class TarifaCalculacionMoveTest(unittest.TestCase):
        def test_tarifa_calcula_move(self):
            calculator = TaxiTarifaCalculador()
            start_time = time.time()
            stop_time = start_time + 20
            si_moeve = True
            tarifa_esperada = 1

            # Call to the tarifa calculation
            tarifa_actual = asyncio.run(calculator.calcular_tarifa(start_time, stop_time, si_moeve))

            # Checking if expectada equal to calculated
            self.assertAlmostEqual(tarifa_actual, tarifa_esperada, places=2)


if __name__ == '__main__':
    unittest.main()
