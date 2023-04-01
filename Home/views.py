from django.shortcuts import render
from django.views import View
from Works.models import Product, Category
from django.shortcuts import get_object_or_404


def for_all_pages(request):
    categories = Category.objects.all()
    return {"categories": categories}


class HomeView(View):
    def get(self, request):
        product = Product.objects.all()
        return render(request, 'Home/home.html', {'products': product})


class CategoryView(View):
    def get(self, request, category_name):
        category = get_object_or_404(Category, name=category_name)
        prduct = Product.objects.filter(category=category)
        return render(request, 'Home/category.html', {'products': prduct, 'category': category})