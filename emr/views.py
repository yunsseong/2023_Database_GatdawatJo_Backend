from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *

# class ViewSet(viewsets.ModelViewSet):
#     queryset = .objects.all()
#     serializer_class = Serializer

class PatientIdentityViewSet(viewsets.ModelViewSet):
    queryset = PatientIdentity.objects.all()
    serializer_class = PatientIdentitySerializer
    filterset_fields = ('patient_id',)
    
    # def perform_create(self, serializer):
    #     ins = serializer.save()
    #     reception_instance = PatientStatus(patient_id=ins.patient_id, patient_name=ins.patient_name, status="접수")
    #     reception_instance.save()

class PatientListViewSet(viewsets.ModelViewSet):
    queryset = PatientList.objects.all()
    serializer_class = PatientListSerializer

class PatientReceptionViewSet(viewsets.ModelViewSet):
    queryset = PatientReception.objects.all()
    serializer_class = PatientReceptionSerializer
    filterset_fields = ('patient',)

    # def perform_create(self, serializer):
    #     print(self.request)
    #     serializer.save(patient = self.request.patient)

class PatientStatusViewSet(viewsets.ModelViewSet):
    queryset = PatientStatus.objects.all()
    serializer_class = PatientStatusSerializer

class MedicalPersonIdentityViewSet(viewsets.ModelViewSet):
    queryset = MedicalPersonIdentity.objects.all()
    serializer_class = MedicalPersonIdentitySerializer

class PatientChartViewSet(viewsets.ModelViewSet):
    queryset = PatientChart.objects.all()
    serializer_class = PatientChartSerializer
    filterset_fields = ('patient',)

class InspectViewSet(viewsets.ModelViewSet):
    queryset = Inspect.objects.all()
    serializer_class = InspectSerializer

class InspectTypeViewSet(viewsets.ModelViewSet):
    queryset = InspectType.objects.all()
    serializer_class = InspectTypeSerializer

class PatientInbodyViewSet(viewsets.ModelViewSet):
    queryset = PatientInbody.objects.all()
    serializer_class = PatientInbodySerializer

class PatientBloodViewSet(viewsets.ModelViewSet):
    queryset = PatientBlood.objects.all()
    serializer_class = PatientBloodSerializer

class DiseaseViewSet(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializers_class = DiseaseSerializer

class TreatmentViewSet(viewsets.ModelViewSet):
    queryset = Treatment.objects.all()
    serializers_class = TreatmentSerializer

class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializers_class = MedicationSerializer

class Image(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializers_class = ImageSerializer


