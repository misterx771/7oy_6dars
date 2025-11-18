from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Company, Employee
from .serializers import CompanySerializer, EmployeeSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        company = self.get_object()
        employees = company.employees.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def name_only(self, request, pk=None):
        company = self.get_object()
        return Response({"company_name": company.name})

    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        company = self.get_object()
        company.is_active = True
        company.save()
        return Response({"status": "Activated"})

    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        company = self.get_object()
        company.is_active = False
        company.save()
        return Response({"status": "Deactivated"})

    @action(detail=False, methods=['get'])
    def stats(self, request):
        total = Company.objects.count()
        return Response({"total_companies": total})


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
