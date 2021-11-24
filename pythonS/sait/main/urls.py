from django.urls import path
from . import views


app_name = 'main'
urlpatterns = [
    path('', views.start, name='start'),
    path('list_rap', views.list_rap, name='list_rap'),
    path('raper/<int:id_r>', views.raper, name='raper'),
    #path('poisk', views.poisk, name='poisk')
]
