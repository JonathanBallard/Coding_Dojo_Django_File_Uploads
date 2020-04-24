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
        print('YES POST')
        form = UploadFileForm(request.POST, request.FILES)
        print('***************************request.FILES:')
        print(request.FILES)

        if form.is_valid():
            print('valid file')
            handle_uploaded_file(request.FILES['file'])
            return redirect('/file/file/')
    else:
        print('NOT POST')
        form = UploadFileForm()
    return render(request, 'file_app/upload.html', {'form': form})



def index(request): 
    return render(request, 'file_app/index.html') 

def uploadFile(request):
    return redirect('/file/')

def showFile(request):

    file = 0

    context = {
        "file" : file,

    }

    return render(request, 'file_app/file.html', context)














