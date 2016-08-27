import unittest
from bin.estudiante import Estudiante
class EstudianteTest(unittest.TestCase):
    def testGetCarreraEmpty(self):
        estudiante1 = Estudiante('Prueba',22,'prueba@ejemplo.com')
        self.assertEqual(estudiante1.getCarreras(),[])
    def testGetCarrera(self):
        estudiante1 = Estudiante('Prueba',22,'prueba@ejemplo.com',['Fisica Nuclear'])
        self.assertEqual(estudiante1.getCarreras(),['Fisica Nuclear'])
    def testSetCarrera(self):
        estudiante1 = Estudiante('Prueba',22,'prueba@ejemplo.com')
        self.assertEqual(estudiante1.getCarreras(),[])
        estudiante1.addCarrera('Literatura')
        self.assertEqual(estudiante1.getCarreras(),['Literatura'])