from django.urls import path
from . import views

urlpatterns = [
    path('', views.patients_home, name='patients'),
    path('scan/', views.scan, name='scan'),
    path('<int:pk>', views.PatientsDetail.as_view(), name='patients_detail'),
    path('<int:pk>/delete', views.PatientsDelete.as_view(), name='patients_delete')
]
