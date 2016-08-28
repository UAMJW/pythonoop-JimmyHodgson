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
    def testSetCarreraDuplicate(self):
        estudiante1 = Estudiante('Prueba',22,'prueba@ejemplo.com')
        self.assertEqual(estudiante1.addCarrera('Sistemas'),0)
        self.assertEqual(estudiante1.addCarrera('Sistemas'),1)
        self.assertEqual(estudiante1.getCarreras(),['Sistemas'])
    def testSetCarreraMax(self):
        estudiante1 = Estudiante('Prueba',22,'prueba@ejemplo.com')
        self.assertEqual(estudiante1.getCarreras(),[])
        self.assertEqual(estudiante1.addCarrera('Sistemas'),0)
        self.assertEqual(estudiante1.addCarrera('Literatura'),0)
        self.assertEqual(estudiante1.addCarrera('Derecho'),1)
        self.assertEqual(estudiante1.getCarreras(),['Sistemas','Literatura'])
    def testRemoveCarrera(self):
        estudiante1 = Estudiante('Prueba',22,'prueba@ejemplo.com',['Sistemas'])
        self.assertEqual(estudiante1.getCarreras(),['Sistemas'])
        self.assertEqual(estudiante1.removeCarrera('Sistemas'),0)
        self.assertEqual(estudiante1.getCarreras(),[])
        self.assertEqual(estudiante1.removeCarrera('Sistemas'),1)
        self.assertEqual(estudiante1.getCarreras(),[])
        
        
