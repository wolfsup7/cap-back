from django.urls import path
from . import views


urlpatterns = [
    path('clients', views.ClientList.as_view(), name='client_list'),
    path('clients/<int:pk>', views.ClientDetail.as_view(), name='client_detail'),
]