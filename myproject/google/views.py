from django.shortcuts import render
from .models import *  ## Importing all models from the current app's models.py file

def category_products(request):
    categories = Category.objects.prefetch_related('products').all()
    return render(request, 'category_products.html', {'categories': categories})

def students_list(request):
    students = Student.objects.all()
    return render(request, 'students_list.html', {'students': students})
