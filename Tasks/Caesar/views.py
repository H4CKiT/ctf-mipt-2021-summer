from django.http import HttpResponse


def index(request):
    file = open('Caesar/caesar_encoded.txt', 'r')
    return HttpResponse(file.read())
