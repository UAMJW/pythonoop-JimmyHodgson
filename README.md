# Tarea 1. Clases En Python

El objetivo de esta tarea es el de aprender los conceptos básicos del lenguaje Python e implementarlos para generar una clase funcional.

| Autor | versión | Licensia | Fecha |
| --- | --- | --- | --- |
| [Jimmy Hodgson](https://github.com/JimmyHodgson) | 1.0.0 | GPLv3 | 2016-08-26 |

---

## Hello World en Python
```python

print 'Hello, World!'

```
## Estructura de una clase
```python
class myClass(object):
    def __init__(self,valor):
        #constructor
        self.propiedad = valor
    def method(self):
        #método que imprime en pantalla la propiedad de la clase
        print self.propiedad
        
```

## Guía de Ejecución

Para ejecutar el proyecto debemos abrir la consola de comandos y ejecutar el siguiente comando:

```
> python main.py
```

Para ejecutar las pruebas se debe ejecutar el siguiente comando desde la consola
```
> python -m test.runner
```
