# this page was created to add custom patterns as development progress
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('patients/', views.PatientListView.as_view(), name='patients'),
    path('patient/<int:pk>', views.PatientDetailView.as_view(), name='patient-details'),
    path('devices/', views.DeviceListView.as_view(), name='devices'),
    path('device/<int:pk>', views.DeviceDetailView.as_view(), name='device-detail'),
]

# for create and delete device
urlpatterns += [  
    path('device/create/', views.DeviceCreate.as_view(), name='device_create'),
    path('device/<int:pk>/update/', views.DeviceUpdate.as_view(), name='device_update'),
    path('device/<int:pk>/delete/', views.DeviceDelete.as_view(), name='device_delete'),
]

# for create and delete patient details
urlpatterns += [  
    path('patient/create/', views.PatientCreate.as_view(), name='patient_create'),
    path('patient/<int:pk>/update/', views.PatientUpdate.as_view(), name='patient_update'),
    path('patient/<int:pk>/delete/', views.PatientDelete.as_view(), name='patient_delete'),
]