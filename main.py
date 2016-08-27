from bin.estudiante import Estudiante
from bin.profesor import Profesor

estudiantes = []
profesores = []

def mainSwitch(option):
    return {
        '1':crear_estudiante,
        '2':crear_profesor,
        '3':listar_estudiantes,
        '4':listar_profesores,
        '99':endFunction
    }.get(option,default)

def endFunction():
    print 'Hasta luego!'
    print ''

def default():
    print 'Oops, opcion no valida.'
    print ''

def crear_estudiante():
    nombre = raw_input('Ingrese el nombre del estudiante: ')
    edad   = raw_input('Ingrese la edad del estudiante: ')
    correo = raw_input('Ingrese el correo del estudiante: ')
    carrera = raw_input('Ingrese la carrera del estudiante: ')

    estudianteNuevo = Estudiante(nombre,edad,correo,[carrera])
    estudiantes.append(estudianteNuevo)
    print ''

def crear_profesor():
    nombre = raw_input('Ingrese el nombre del profesor: ')
    edad   = raw_input('Ingrese la edad del profesor: ')
    correo = raw_input('Ingrese el correo del profesor: ')
    facultad = raw_input('Ingrese la facultad del profesor: ')

    profesorNuevo = Profesor(nombre,edad,correo,facultad)
    profesores.append(profesorNuevo)
    print ''
def listar_estudiantes():
    for estudiante in estudiantes:
        print estudiante.toString()
    print ''
    raw_input('presione cualquier tecla para continuar...') 

def listar_profesores():
    for profesor in profesores:
        print profesor.toString()
    print ''
    raw_input('presione cualquier tecla para continuar...')

def printMenu():
    print '#################################'
    print '#        MENU PRINCIPAL         #'
    print '#################################'
    print '     1. Crear Estudiante'
    print '     2. Crear Profesor'
    print '     3. Listar Estudiantes'
    print '     4. Listar Profesores'
    print '    99. Salir'
    print ''


var = ''
while (var!='99'):
    printMenu()
    var = raw_input('Que desea hacer?: ')
    mainSwitch(var)()

