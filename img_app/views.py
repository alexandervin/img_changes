from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView, CreateView, UpdateView, DetailView

from .forms import ImageFormAdd, ImageUpdateForm
from .models import ImageModel, ImageUpdate


def index(request):
    """ Контроллер отображения добавленных изображений на главной странице """
    data = ImageModel.objects.all()
    context = {'data': data}
    return render(request, 'img_app/index.html', context)


class CreateImgView(FormView):
    """ Контроллер отображения формы и сохранение img в БД """
    model = ImageModel
    form_class = ImageFormAdd
    template_name = 'img_app/add_img.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['images'] = ImageModel.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        self.object = super().get_form(form_class)
        return self.object

    def get_success_url(self):
        return reverse('img_app:resize_img', kwargs={'images': self.object.image_loc.pk})


def resize_img(request, pk):
    """ Контроллер класс изменения размеров изображений """
    imgm = ImageModel.objects.get(pk=pk)
    if request.method == 'POST':
        imgf = ImageUpdateForm(request.POST, instance=imgm)
        if imgf.is_valid():
            imgf.save()
            return HttpResponseRedirect(reverse('img_app:resize_img',
                                                kwargs={'image': imgf.cleaned_data['image_id'].pk}))
        else:
            context = {'form': imgf}
            return render(request, 'img_app/resize_img.html', context)
    else:
        imgf = ImageUpdateForm(instance=imgm)
        context = {'form': imgf}
        return render(request, 'img_app/resize_img.html', context)
