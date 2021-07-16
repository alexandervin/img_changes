from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView, CreateView

from .forms import ImageFormAdd
from .models import ImageModel


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
    #imgm =
    #imgf = ImageFormAdd(request.POST)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        self.object = super().get_form(form_class)
        return self.object

    def get_success_url(self):
        return reverse('img_app:resize_img')
        # return HttpResponseRedirect(reverse('img_app:resize_img',
        #                                     kwargs={'imagemodel_id': bbf.cleaned_data['rubric'].pk}))

def resize_img(request):
    """ Контроллер изменения размеров изображений """
    return render(request, 'img_app/resize_img.html')

# def edit(request, pk):
    # bb = Bb.objects.get(pk=pk)
    # if request.method == 'POST’:
        # bbf = BbForm(request.POST, instance=bb)
        # if bbf.is_valid():
            #if bbf.has_changed():
                # bbf.save()
                # return HttpResponseRedirect(reverse(’bboard:by_rubric*,
                    # kwargs={’rubric_id’: bbf.cleaned_data[’rubric’].pk}))
    # else:
        # context = {’form': bbf}
        # return render(request, 'bboard/bb_form.html’, context)
    # else:
        # bbf = BbForm(instance=bb)
        # context = {'form': bbf}
        # return render(request, 'bboard/bb_form.html', context)
















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

# https://fixmypc.ru/post/zagruzka-izobrazhenii-i-drugikh-failov-v-django-3-cherez-formy-i-modeli/

# def get_remote_image(self):
#     if self.image_url and not self.image_file:
#         result = urllib.request.urlopen(self.image_url)
#         self.image_file.save(
#             os.path.basename(self.image_url),
#             File(open(result[0]))
#         )
#         self.save()

# def get_img(self):
#
#     url = self.image_url
#     try:
#         resp = requests.get(url, stream=True).raw
#     except requests.exceptions.RequestException as e:
#         sys.exit(1)
#     try:
#         img = Image.open(resp)
#     except IOError:
#         print("Unable to open image")
#         sys.exit(1)
#     return img.save(self.image_file, 'jpeg')
