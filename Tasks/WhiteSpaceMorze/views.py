from django.http import HttpResponse


def index(request):
    file = open('WhiteSpaceMorze/caesar_encoded.txt', 'r')
    return HttpResponse(file.read())
