from django.http import HttpResponse


def crypto(request):
    file = open('Vegenere/crypto', 'r')
    return HttpResponse(file.read())
