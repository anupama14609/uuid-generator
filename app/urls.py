from django.urls import path
from .views import home , GenerateId

urlpatterns = [ 
    path('', home, name="home"),
    path('generate-id', GenerateId, name='generate-id')
]
