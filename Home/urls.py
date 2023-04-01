from django.urls import path
from .views import HomeView, CategoryView

app_name = 'Home'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('<str:category_name>/category/', CategoryView.as_view(), name='category'),
]