from django.http import FileResponse


def index(request):
    file = open('Stego/hackerman.png', 'rb')
    return FileResponse(file)
