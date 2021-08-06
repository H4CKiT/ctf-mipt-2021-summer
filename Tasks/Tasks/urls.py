from django.urls import path, include

urlpatterns = [
    path('caesar/', include('WhiteSpaceMorze.urls')),
    path('zipper/', include('Zipper.urls'))
]
