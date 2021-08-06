from django.urls import path, include

urlpatterns = [
    path('caesar/', include('Caesar.urls')),
    path('zipper/', include('Zipper.urls')),
    path('stego/', include('Stego.urls')),
    path('pyc/', include('Pyc.urls')),
]
