from .models import Catalog, Property
from .serializers import CatalogSerializer, PropertySerializer, PropertyDetailsSerializer
from rest_framework import generics


class CatalogListAPIView(generics.ListAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer


class PropertyListAPIView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class PropertyRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyDetailsSerializer
