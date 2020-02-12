from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views import View
from PIL import Image
from django.http import HttpResponseRedirect

# Create your views here.
class IndexView(View):

    def get(self, request):
        form = IndexForm()
        return render(request, 'handwriting_recognition/index.html', {'form': form})

    def post(self, request):
        form = IndexForm(request.POST)
        if form.is_valid():
            image = form.cleaned_data['img']
            img = Image.open(image)
            img.save('C:\PythonCourse\finalproject\finalproject\handwriting_recognition\static\media','jpeg')
        return HttpResponseRedirect('/processing/')


def img_to_text():
    pass


def processing(request):
    #img_to_text()
    context = dict()
    context['text'] = "Processing"
    return render(request, 'handwriting_recognition/processing.html', context)


def show_output(self, request, text_data ="No text"):
    context = dict()
    context['text'] = text_data
    return render(request, 'handwriting_recognition/output.html', context)


def savingPDF(self, request, text_data="No text"):
