from django.shortcuts import render

from .models import Courses

from django.views.generic import DetailView

def courses_list(request):
    courses = Courses.objects.all()
    return render(request, 'products/products.html', {'courses': courses})

def courses_description(request):
    return render(request, 'products/product.html')

class URL_DetailView(DetailView):
    model = Courses
    template_name = 'products/product.html'
    context_object_name = 'product'