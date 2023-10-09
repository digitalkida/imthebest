from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'frontend/index.html')

def about(request):
    return render(request, 'frontend/about.html')

def works(request):
    return render(request, 'frontend/works.html')

def contact(request):
    return render(request, 'frontend/contact.html')