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
    all_brands = Brand.objects.all()

    passing_dict = {
        "all_brands": all_brands
    }
    return render(request, 'core/brand.html', passing_dict)


def news(request):
    passing_dict = {
        
    }
    return render(request, 'core/news.html')

def contact(request):
    passing_dict = {

    }
    return render(request, 'core/contact.html')

def brand_detail(request, pk):
    brand = Brand.objects.get(pk=pk)
    passing_dict = {
        "brand": brand
    }
    return render(request, 'core/brand_detail.html', passing_dict)
