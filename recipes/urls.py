from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:recipe_id>/', views.recipes, name='recipe'),
    path('recipes/category/<int:category_id>/', views.category, name="category"),
]
