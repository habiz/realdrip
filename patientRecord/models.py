from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
# Models for type of disease admitted for in the clinic
class Diagnosis(models.Model):

    name = models.CharField(max_length=200, help_text="Enter the diagnosis ailments for (e.g stroke, Venous Thromboembolism,etc)")
# represent the model clearly in the admin dashboard
    def __str__(self):
        return self.name

#Models for patient and their details

class Patient(models.Model):

    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    GENDER_STATUS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_STATUS, blank=True, default='M', help_text="Male/Female")
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=300)
    summary = models.TextField(max_length=1000, help_text="Enter the brief details about the disease/ reason for admission")
    ClinicID = models.CharField('CLINICID',max_length=13, help_text="Enter the clinic unique ID")
    device = models.ForeignKey('Device', on_delete=models.SET_NULL, null=True)
    diagnosis = models.ManyToManyField(Diagnosis, help_text="Enter the diagnosis type for the patient")

    def __str__(self):

        return self.firstname

    def get_absolute_url(self):

        return reverse('patient-details', args=[str(self.id)])

    def display_diagnosis(self):

        return ', '.join([ disease.name for disease in self.diagnosis.all()[:3]])
    display_diagnosis.short_description = 'Diagnosis'
    

class PatientInstance(models.Model):

    card_number = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for a particular treatment case")
    patient = models.ForeignKey('Patient', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    discharge_time = models.DateField(null=True, blank=True)

    HEALTH_STATUS = (
        ('A', 'Admitted'),
        ('T', 'Treatment'),
        ('D', 'Discharge'),
    )

    status = models.CharField(max_length=1, choices=HEALTH_STATUS, blank=True, default='A', help_text="Patient Condition")

    class Meta:
        ordering = ['discharge_time']

    def __str__(self):

        return '{0} ({1})'.format(self.id,self.patient.firstname)

#model for devices in the clinic
class Device(models.Model):

    device_name = models.CharField(max_length=200)
    number_id = models.CharField(max_length=200)
    clinic_name = models.CharField(max_length=200)
    date_of_purchase = models.DateField('Purchase date', null=True, blank=True)

    class Meta:
        ordering = ["number_id","device_name"]

    def get_absolute_url(self):
        
        return reverse('device-detail', args=[str(self.id)])

    def __str__(self):

        return '{0}, {1}'.format(self.number_id,self.device_name)
