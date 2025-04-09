from subprocess import run, PIPE
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import City, IDC, Host
from .serializers import CitySerializer, IDCSerializer, HostSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class IDCViewSet(viewsets.ModelViewSet):
    queryset = IDC.objects.all()
    serializer_class = IDCSerializer


class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer

    @action(detail=True, methods=['get'])
    def ping(self, request, pk=None):
        host = self.get_object()
        result = run(['ping', '-c', '1', host.name], stdout=PIPE)
        return Response({'reachable': result.returncode == 0})
