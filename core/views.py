from django.shortcuts import render
from .models import Retailers, Feedback, Brand, Contact
from django.utils import timezone


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


def add_contact(request):
    if request.method == 'POST':
        if request.POST['full_name'] and request.POST['email'] and request.POST['message']:
            contact = Contact()
            contact.full_name = request.POST['full_name']
            contact.phone_number = request.POST['phone_number']
            contact.email = request.POST['email']
            contact.company = request.POST['company']
            contact.message = request.POST['message']
            contact.date = timezone.datetime.now()
            contact.save()

            error_msg = "Thank you for getting in touch!"
            error_type = 0

            return render(request, 'core/contact.html', {
                "error_msg": error_msg,
                "error_type": error_type
            })
        else:
            error_msg = "Something went wrong. Please try again."
            error_type = 1
            print(error_msg)
            return render(request, 'core/contact.html', {
                "error_msg": error_msg,
                "error_type": error_type
            })
    else:
        return render(request, 'core/contact.html')
