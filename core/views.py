from django.shortcuts import render

def home(request):
    passing_dict = {
        
    }
    return render(request, 'core/home.html')


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
