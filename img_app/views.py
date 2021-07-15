from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView

from .forms import ImageFormAdd
from .models import ImageModel

def index(request):
    data = ImageModel.objects.all()
    context = {'data': data}
    return render(request, 'img_app/index.html', context)


class CreateImgView(FormView,):
    model = ImageModel
    form_class = ImageFormAdd
    template_name = 'img_app/add_img.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        self.object = super().get_form(form_class)
        return self.object

    def get_success_url(self):
        return reverse('img_app:resize_img')



def resize_img(request):
    return render(request, 'img_app/resize_img.html')

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

#https://fixmypc.ru/post/zagruzka-izobrazhenii-i-drugikh-failov-v-django-3-cherez-formy-i-modeli/