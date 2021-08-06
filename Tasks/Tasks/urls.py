from django.urls import path, include
from .views import crypto


urlpatterns = [
    path('caesar/', include('Caesar.urls')),
    path('zipper/', include('Zipper.urls')),
    path('stego/', include('Stego.urls')),
    path('pyc/', include('Pyc.urls')),
    path('crypto/', crypto),
]
