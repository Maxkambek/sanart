from .serializers import ContactSerializer, GetInTouchSerializer, NewsSerializer
from .models import Contact, News, GetInTouch
from rest_framework import generics


class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class ContactListAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class GetInTouchCreateAPIView(generics.CreateAPIView):
    queryset = GetInTouch.objects.all()
    serializer_class = GetInTouchSerializer


