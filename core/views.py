from django.shortcuts import render
from .models import Retailers

def home(request):
    all_retailers = Retailers.objects.all()
    print(all_retailers)
    passing_dict = {
        "all_retailers": all_retailers
    }
    return render(request, 'core/index.html', passing_dict)


def about(request):
    passing_dict = {
        
    }
    return render(request, 'core/about.html')


def brand(request):
    passing_dict = {
        
    }
    return render(request, 'core/brand.html')


def news(request):
    passing_dict = {
        
    }
    return render(request, 'core/news.html')
