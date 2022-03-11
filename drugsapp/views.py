from rest_framework import mixins, viewsets
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.viewsets import ModelViewSet

from .models import Drug, FormOfRelease, Patient, PrescriptionDrug, Recipe
from .serializers import (DrugSerializer, FormOfReleaseSerializer,
                          PatientSerializer, PrescriptionDrugSerializer,
                          RecipeSerializer)


class DrugModelViewSet(ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

class FormOfReleaseModelViewSet(ModelViewSet):
    queryset = FormOfRelease.objects.all()
    serializer_class = FormOfReleaseSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

class PatientModelViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    
class PrescriptionDrugModelViewSet(ModelViewSet):
    queryset = PrescriptionDrug.objects.all()
    serializer_class = PrescriptionDrugSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    
class RecipeModelViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
