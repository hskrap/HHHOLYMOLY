from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def TEST1(request):
    return render(request,'TEST1.html')