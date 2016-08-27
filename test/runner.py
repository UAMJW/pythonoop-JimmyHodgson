from unittest import TestLoader, TextTestRunner, TestSuite
from estudianteTest import EstudianteTest
from personaTest import PersonaTest

if __name__ == "__main__":

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(EstudianteTest),
        loader.loadTestsFromTestCase(PersonaTest),
        ))

    runner = TextTestRunner(verbosity = 2)
    runner.run(suite)