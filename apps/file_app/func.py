






def handle_uploaded_file(f):
    with open('file_app/test.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)




