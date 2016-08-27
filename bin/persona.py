class Persona(object):
    def __init__(self,nombre,edad,correo):
        self.__nombre = nombre
        self.__edad   = edad
        self.__correo = correo

    def getNombre(self):
        return self.__nombre
    def getEdad(self):
        return self.__edad
    def getCorreo(self):
        return self.__correo
    def setNombre(self,nombre):
        self.__nombre = nombre
    def setEdad(self,edad):
        self.__edad = edad
    def setCorreo(self,correo):
        self.__correo = correo
    def toString(self):
        return self.__nombre+' - '+str(self.__edad)+' - '+self.__correo