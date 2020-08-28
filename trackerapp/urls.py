from django.urls import path
from trackerapp import views as v

urlpatterns = [
    path('', v.index, name='homepage')
]
