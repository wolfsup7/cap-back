from django.urls import path
from . import views


urlpatterns = [
    path('api/clients', views.ClientList.as_view(), name='client_list'),
    path('api/clients/<int:pk>', views.ClientDetail.as_view(), name='client_detail'),
]
