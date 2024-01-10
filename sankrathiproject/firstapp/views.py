from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'firstapp/home.html')
def index_view(request):
    return render(request,'firstapp/index.html')
