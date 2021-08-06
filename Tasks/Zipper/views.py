from django.http import FileResponse


def index(request):
    file = open('Zipper/ultra_zipper_text.png', 'rb')
    return FileResponse(file)
