from django.shortcuts import render


# Create your views here.
def index(request):
    
    return render(request, 'index.html', {'autos':autos})

class Auto:
    def __init__(self, nombre, modelo, precio, color, img_url):
        self.nombre=nombre
        self.modelo=modelo
        self.precio=precio
        self.color=color
        self.img_url=img_url

image="https://img.motoryracing.com/noticias/portada/23000/23731-n.jpg"
autos=[
  Auto("VW jetta", 2018, 145500, "rojo", image),  
  Auto("Futura", 1955, 0, "aqua", image), 
  Auto("Seat", 2001, 11000, "azul", image), 
  Auto("Ford", 1999, 34000, "negro", image), 

]


