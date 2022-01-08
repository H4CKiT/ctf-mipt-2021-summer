from django.urls import path, include
from .views import crypto, rsa0, rsa1, stego


urlpatterns = [
    path('caesar/', include('Caesar.urls')),
    path('zipper/', include('Zipper.urls')),
    path('stego/', stego),
    path('pyc/', include('Pyc.urls')),
    path('crypto/', crypto),
    path('rsa0/', rsa0),
    path('rsa1/', rsa1),
]
