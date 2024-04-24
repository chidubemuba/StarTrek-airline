from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='flights_index'),
    path('<int:flight_id>', views.flight, name='flight'),
    path('<int:flight_id>', views.book, name='book')
]

