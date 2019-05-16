from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View

import time

from .models import FileUpload
from .forms import FileForm

# def testingUrl(request):
#     return HttpResponse("Welcome")


class UploadView(View):
    def get(self, request):
        photos_list = FileUpload.objects.all()
        return render(self.request, 'fileupload/index.html',
                      {'photos': photos_list})
