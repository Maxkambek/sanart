from .models import Catalog, Property, CatalogVideo
from .serializers import CatalogSerializer, PropertySerializer, PropertyDetailsSerializer, CatalogVideoSerializer, \
    PropertyDetailSerializer
from rest_framework import generics


class CatalogVideoListAPIView(generics.ListAPIView):
    serializer_class = CatalogVideoSerializer

    def get_queryset(self):
        queryset = CatalogVideo.objects.all()
        catalog = self.request.GET.get('catalog_id')
        if catalog:
            queryset = queryset.filter(catalog_id=catalog)
        return queryset


class CatalogListAPIView(generics.ListAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer


class PropertyListAPIView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class PropertyRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyDetailSerializer
