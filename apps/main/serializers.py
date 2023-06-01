from .models import PropertyDetails, Property, PropertyFiles, PropertyImages, Catalog
from rest_framework import serializers


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['id', 'name', 'image']


class PropertyFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyFiles
        fields = ['id', 'file']


class PropertyImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImages
        fields = ['id', 'image']


class PropertyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyDetails
        fields = ['id', 'text']


class PropertyDetailSerializer(serializers.ModelSerializer):
    property_images = PropertyImagesSerializer(many=True)
    property_details = PropertyDetailsSerializer(many=True)
    property_files = PropertyFilesSerializer(many=True)

    class Meta:
        model = Property
        fields = ['id', 'name', 'sort_number', 'views', 'deadline',
                  'start_price', 'trade_type',
                  'trade_style', 'start_date',
                  'back_price', 'get_first_step_price',
                  'address', 'catalog', 'description', 'phone', 'status',
                  'property_images', 'property_details', 'property_files'
                  ]


class PropertySerializer(serializers.ModelSerializer):
    property_images = PropertyImagesSerializer(many=True)

    class Meta:
        model = Property
        fields = ['id', 'name', 'sort_number', 'views', 'deadline',
                  'start_price',
                  'start_date',
                  'back_price',
                  'address',
                  'property_images',
                  ]
