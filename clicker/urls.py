from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    # REST API URLS
    path('increase/', views.increase, name='increase'),
    path('decrease/', views.decrease, name='decrease'),
    path('update/', views.update, name='update'),
]
