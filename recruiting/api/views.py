from rest_framework import generics
from rest_framework import permissions

from recruiting.api.serializers import VacancySerializer
from recruiting.models import Vacancy


class VacancyList(generics.ListAPIView):

    queryset = Vacancy.objects.filter(is_active=True)
    serializer_class = VacancySerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Vacancy.objects.filter(is_active=True)
        location = self.request.query_params.get('location', None)
        if location is not None:
            queryset = queryset.filter(location__name__icontains=location)

        company = self.request.query_params.get('company', None)
        if company is not None:
            queryset = queryset.filter(company__name__icontains=company)
        return queryset


class VacancyUpdate(generics.RetrieveUpdateDestroyAPIView):

    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

