from django.shortcuts import render


# Create your views here.
def index(request):
    
    return render(request, 'index.html', {'autos':autos})

class Auto:
    def __init__(self, nombre, modelo, precio, color):
        self.nombre=nombre
        self.modelo=modelo
        self.precio=precio
        self.color=color

autos=[
  Auto("VW jetta", 2018, 145500, "rojo")  
  Auto("Futura", 1955, 0, "aqua")
  Auto("Seat", 2001, 11000, "azul")
  Auto("Ford", 1999, 34000, "negro")

]
a=Auto("VW jetta", 2018, 145500, "rojo")

