from django.http import HttpResponse


def crypto(request):
    file = open('Vegenere/crypto', 'r')
    return HttpResponse(file.read())

def rsa0(request):
    file = open('RSA/rsa0.txt', 'r')
    return HttpResponse(file.read())

def rsa1(request):
    file = open('RSA/rsa1.zip', 'rb')
    response =  HttpResponse(file.read(), content_type='application/zip')
    filename = 'rsa1.zip'
    response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
    return response

def stego(request):
    file = open('Stego/hackerman.png', 'rb')
    return FileResponse(file)