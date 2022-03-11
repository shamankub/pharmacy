from rest_framework import mixins, viewsets
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.viewsets import ModelViewSet

from .models import Branch, Position, Salary, Staff, Vacation
from .serializers import (BranchSerializer, PostionSerializer,
                          SalarySerializer, StaffSerializer,
                          VacationSerializer)


class StaffModelViewSet(ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

class PositionModelViewSet(ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PostionSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

class BranchModelViewSet(ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    
class VacationModelViewSet(ModelViewSet):
    queryset = Vacation.objects.all()
    serializer_class = VacationSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    
class SalaryModelViewSet(ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
