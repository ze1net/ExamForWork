from django.urls import path
from .views import menu_page

app_name = 'menu'

urlpatterns = [
    path('<name>', menu_page, name='menu_page'),
]
