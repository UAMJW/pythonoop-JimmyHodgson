import unittest
from bin.persona import Persona
class PersonaTest(unittest.TestCase):
    def testGetName(self):
        persona1 = Persona('Prueba',22,'prueba@ejemplo.com')
        self.assertEqual(persona1.getNombre(),'Prueba')

    def testGetsEdad(self):
        persona1 = Persona('Prueba',22,'prueba@ejemplo.com')
        self.assertEqual(persona1.getEdad(),22)

    def testGetsCorreo(self):
        persona1 = Persona('Prueba',22,'prueba@ejemplo.com')
        self.assertEqual(persona1.getCorreo(),'prueba@ejemplo.com')

    def testsetName(self):
        persona1 = Persona('Prueba',22,'prueba@ejemplo.com')
        self.assertEqual(persona1.getNombre(),'Prueba')
        persona1.setNombre('Jimmy')
        self.assertEqual(persona1.getNombre(),'Jimmy')
        

    def testsetsEdad(self):
        persona1 = Persona('Prueba',22,'prueba@ejemplo.com')
        self.assertEqual(persona1.getEdad(),22)
        persona1.setEdad(25)
        self.assertEqual(persona1.getEdad(),25)

    def testsetsCorreo(self):
        persona1 = Persona('Prueba',22,'prueba@ejemplo.com')
        self.assertEqual(persona1.getCorreo(),'prueba@ejemplo.com')
        persona1.setNombre('cambio@ejemplo.com')
        self.assertEqual(persona1.getNombre(),'cambio@ejemplo.com')
