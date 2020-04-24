# Using Django Messages: https://docs.djangoproject.com/en/1.11/ref/contrib/messages/#displaying-messages 
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse, redirect, render

from django.template import RequestContext
from django.urls import reverse

from .forms import *

from .models import *

# from .forms import UploadFileForm
# Imaginary function to handle an uploaded file.
# from .func import handle_uploaded_file


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


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()


    # Render list page with the documents and the form
    return render(request, 'file_app/index.html', {'documents': documents, 'form': form})

















