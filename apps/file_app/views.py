from django.shortcuts import render, redirect, HttpResponse 
# Using Django Messages: https://docs.djangoproject.com/en/1.11/ref/contrib/messages/#displaying-messages 
from django.contrib import messages 
from .models import * 

from django.http import HttpResponseRedirect
from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
from .func import handle_uploaded_file


# Create your views here. 
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/file/')
    else:
        form = UploadFileForm()
    return render(request, 'file_app/upload.html', {'form': form})



def index(request): 
    return render(request, 'file_app/index.html') 

def uploadFile(request):
    return redirect('/file/')














