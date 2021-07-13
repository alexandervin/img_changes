from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ImageForm
from .models import Image

def index(request):
    data = Image.objects.all()
    context = {'data': data}
    return render(request, 'img_app/index.html', context)


class CreateImgView(CreateView):

    model = Image
    form_class = ImageForm
    template_name = 'img_app/add_img.html'
    success_url = 'img_app/index.html'

# def add_img(request):
#     if request.method == 'POST':
#         form = ImageForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('img_app:index')
#         else:
#             form = ImageForm()
#     context = {'form': form}
#     return render(request, 'img_app/add_img.html', context=context)




def resize_img(request):
    return render(request, 'img_app/resize_img.html')