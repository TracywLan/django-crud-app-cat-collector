from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Cat

# Import HttpResponse to send text-based responses
# from django.http import HttpResponse

# database for cats and define a Cat class
# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age

# Create a list of Cat instances
# cats = [
#     Cat('Lolo', 'tabby', 'Kinda rude.', 3),
#     Cat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
#     Cat('Fancy', 'bombay', 'Happy fluff ball.', 4),
#     Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
# ]

# def cat_index(request):
#     return render(request,'cats/index.html',{'cats':cats})

class CatCreate(CreateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cat_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})

def cat_detail(request):
    cat = Cat.objects.get(id=cat.id)
    return render(request, 'cats/detail.html', {'cats': cat})



