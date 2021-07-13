from django.urls import path

from .views import index, resize_img, CreateImgView

app_name = 'img_app'

urlpatterns = [
    path('', index, name='index'),
    path('add_img/', CreateImgView.as_view(), name='add_img'),
    path('resize_img/', resize_img, name='resize_img'),

]