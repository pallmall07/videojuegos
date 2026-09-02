from django.shortcuts import render
from faker import Faker

def generar_juego(request):
    fake = Faker("es")
    juegos =[]
    for i in range(25):

        juegos.append({
            "nombre": fake.name(),
            "descripcion": fake.text()

        })


    context = {
        "juegos": juegos

    }
    
    return render(request, 'juegos.html', context)
