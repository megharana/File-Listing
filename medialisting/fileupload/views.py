from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import time
import os

from .models import FileUpload
from .forms import FileForm

# def testingUrl(request):
#     return HttpResponse("Welcome")


class UploadView(View):
    def get(self, request):
        file_list = FileUpload.objects.all()

        return render(self.request, 'fileupload/index.html',
                      {'files': file_list})

    def post(self, request):

        time.sleep(1)
        form = FileForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            uploadedFile = form.save()
            data = {
                'is_valid': True,
                'name': uploadedFile.file.name,
                'url': uploadedFile.file.url
            }
        else:
            data = {'is_valid': False}
        return JsonResponse(data)
