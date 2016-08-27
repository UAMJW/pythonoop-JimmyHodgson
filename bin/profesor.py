from persona import Persona
class Profesor(Persona):
    def __init__(self,nombre,edad,correo,facultad):
        Persona.__init__(self,nombre,edad,correo)
        self.__facultad = facultad
    
    def getFacultad(self):
        return self.__facultad
    def setFacultad(self,facultad):
        self.__facultad = facultad

    def toString(self):
        return super(Profesor,self).toString() +' - '+self.__facultad