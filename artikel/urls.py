from django.urls import path
from artikel.views import show_artikel, show_artikel_detail, add, show_json
app_name = 'artikel'

urlpatterns = [
    path('', show_artikel, name='show_artikel'),
    path('<int:pk>', show_artikel_detail, name='detail'),
    path('add/', add, name='add'),
    path('show_json', show_json, name='show_json')

]