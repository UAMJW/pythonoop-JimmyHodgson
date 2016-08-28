from persona import Persona
class Estudiante(Persona):
    def __init__(self,nombre,edad,correo,carreras=None):
        Persona.__init__(self,nombre,edad,correo)
        if(carreras is None):
            carreras=[]
        self.__carreras = carreras

    def getCarreras(self):
        return self.__carreras

    def addCarrera(self,carrera):
        if(len(self.__carreras)<2 and self.__carreras.count(carrera)==0):
            self.__carreras.append(carrera)
            return 0
        else:
            return 1

    def removeCarrera(self,carrera):
        if(len(self.__carreras)>0 and self.__carreras.count(carrera)>0):
            self.__carreras.remove(carrera);
            return 0
        else:
            return 1
    def toString(self):
        return super(Estudiante,self).toString()+' - '+str(self.__carreras)