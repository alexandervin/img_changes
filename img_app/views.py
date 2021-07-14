from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView

from .forms import ImageForm
from .models import Image

def index(request):
    data = Image.objects.all()
    context = {'data': data}
    return render(request, 'img_app/index.html', context)


class CreateImgView(FormView):
    model = Image
    form_class = ImageForm
    template_name = 'img_app/add_img.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        self.object = super().get_form(form_class)
        return self.object

    def get_success_url(self):
        return reverse('img_app:resize_img')



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