from django.urls import path

from .views import index, resize_img, add_img

app_name = 'img_app'

urlpatterns = [
    path('', index, name='index'),
    path('add_img/', add_img, name='add_img'),
    path('resize_img/', resize_img, name='resize_img'),

]