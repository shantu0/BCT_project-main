from django.urls import path
from . import views
from .views import generate_recipe


urlpatterns = [
    path('',views.signupPage,name='signup-page'),
    path('login/',views.loginPage,name='login-page'),
    path('home/',views.home2, name='index-page'),
    path('generate/',views.generate,name="generate-page"),
    path('wishlist/',views.wishlist,name="wishlist-page"),
    path('generate-recipe/', generate_recipe, name='generate_recipe'),
    path('add-to-wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
    path('delete/<int:id>/', views.delete_item, name='delete-page'),

]