from django.http import FileResponse


def crypto(request):
    file = open('Vegenere/crypto', 'rb')
    return FileResponse(file)
