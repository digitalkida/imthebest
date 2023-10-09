from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('works', views.works, name='works'),
    # path('services', views.services, name='services'),
    # path('portfolio', views.portfolio, name='portfolio'),
    # path('blogs', views.blogs, name='blogs'),
    # path('offers', views.offers, name='offers'),
    path('contact', views.contact, name='contact'),
    # path('franchise', views.franchise, name='franchise'),
    # path('orders', views.orders, name='orders'),
    # path('login', views.login, name='login'),
]