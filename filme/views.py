from django.shortcuts import render

# Create your views here.
#função da homepage
def homepage(request): #requisição get para a homepage
  return render(request, "homepage.html")