from django.shortcuts import render
from django.contrib.auth.decorators import login_required #django import support for login required

# Create your views here.

from .models import Patient, Device, PatientInstance, Diagnosis

@login_required #testing required login to access homepage
def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_patients=Patient.objects.all().count()
    num_instances=PatientInstance.objects.all().count()
    # Admitted patient (status = 'a')
    num_instances_admitted=PatientInstance.objects.filter(status__exact='A').count()
    num_devices=Device.objects.all().count()  # The 'all()' is implied by default.

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_patients':num_patients,'num_instances':num_instances,'num_instances_admitted':num_instances_admitted,'num_devices':num_devices, 'num_visits':num_visits},
    )

# view for patients
from django.views import generic

class PatientListView(generic.ListView):
    model = Patient

class PatientDetailView(generic.DetailView):
    model = Patient

class DeviceListView(generic.ListView):
    model = Device

class DeviceDetailView(generic.DetailView):
    model = Device

# create, update and delete realdrip device manager 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Device
from .models import Patient

class DeviceCreate(CreateView):
    model = Device
    fields = '__all__'
    initial={'date_of_purchase':'05/01/2018',}

class DeviceUpdate(UpdateView):
    model = Device
    fields = ['device_name','number_id','clinic_name','date_of_purchase']

class DeviceDelete(DeleteView):
    model = Device
    success_url = reverse_lazy('devices')

#class specifications for patient delete

class PatientCreate(CreateView):
    model = Patient
    fields = ['firstname','lastname','gender','date_of_birth','address','summary','ClinicID']
    initial={'date_of_birth':'05/01/2018',}

class PatientUpdate(UpdateView):
    model = Patient
    fields = ['firstname','lastname','gender','date_of_birth','address','summary','ClinicID','device','diagnosis']

class PatientDelete(DeleteView):
    model = Device
    success_url = reverse_lazy('patients')

