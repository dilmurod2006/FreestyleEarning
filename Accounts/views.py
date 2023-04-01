from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from random import randint
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404
from Works.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import CustomUser, Saved
from .forms import SignUpForm, UpdateProfileForm
# create send mail function

class Register(View):
    def get(self, request):
        return render(request, 'Accounts/registration/register.html', {'form': SignUpForm()})

    def post(self, request):
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account is successfully created.')
            print('Account yaratildi!')
            return redirect('login')
        return render(request, 'Accounts/registration/register.html', {'form': form})

class ProfileView(View):
    def get(self, request, username):
        user = get_object_or_404(CustomUser, username=username)
        return render(request, 'Accounts/profile.html', {'customuser':user})


class UpdateProfileView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        form = UpdateProfileForm(instance=request.user)
        return render(request, 'Accounts/profile_update.html', {'form': form})

    def post(self, request):
        form = UpdateProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account is successfully updated.')
            return redirect('users:profile', request.user)
        return render(request, 'Accounts/registration/register.html', {'form': form})


class AddRemoveSavedView(LoginRequiredMixin, View):
    login_url = "login"

    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        saved_product = Saved.objects.filter(author=request.user, product=product)
        if saved_product:
            saved_product.delete()
            messages.info(request, 'Removed.')
        else:
            Saved.objects.create(author=request.user, product=product)
            messages.info(request, 'Saved.')
        return redirect(request.META.get("HTTP_REFERER"))


class SavedView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        saveds = Saved.objects.filter(author=request.user)
        q = request.GET.get('q', '')
        if q:
            products = Product.objects.filter(title__icontains=q)
            saveds = Saved.objects.filter(author=request.user, product__in=products)
        return render(request, 'Accounts/saveds.html', {"saveds": saveds})


class RecentlyViewedView(View):
    def get(self, request):
        if not "recently_viewed" in request.session:
            products = []
        else:
            r_viewed = request.session["recently_viewed"]
            products = Product.objects.filter(id__in=r_viewed)
            q = request.GET.get('q', '')
            if q:
                products = products.filter(title__icontains=q)
        return render(request, "Accounts/recently_viewed.html", {'products': products})