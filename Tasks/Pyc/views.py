from django.http import FileResponse


def index(request):
    file = open('Pyc/secret_file.pyc', 'rb')
    return FileResponse(file)

