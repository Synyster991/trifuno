from django.shortcuts import render
from .models import Retailers, Feedback, Brand

def home(request):
    all_retailers = Retailers.objects.all()
    all_feedbacks = Feedback.objects.all()
    featured_brands = Brand.objects.all()[:6]
    
    passing_dict = {
        "all_retailers": all_retailers,
        "all_feedbacks": all_feedbacks,
        "featured_brands": featured_brands
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
