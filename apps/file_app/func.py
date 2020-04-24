






def handle_uploaded_file(f):
    print('----------------------------------------------------------')
    print('handle uploaded file!')
    print('----------------------------------------------------------')
    with open('/test.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)




