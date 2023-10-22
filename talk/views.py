from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import action, authentication_classes
from .models import Car, Country, Producter, Comment
from .serializers import CarSerializer, CountrySerializer, ProducterSerializer, CommentSerializer, CarListSerializer, \
    ProducterListSerializer, CommentListSerializer
from rest_framework import viewsets
import csv
from django.http import HttpResponse
from rest_framework.views import APIView


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (AllowAny,)

    def get_authentication_classes(self, request, **kwargs):
        if self.request.method != 'GET':
            authentication_classes.append(TokenAuthentication)
        return authentication_classes

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CarSerializer
        else:
            return CarListSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_authentication_classes(self, request, **kwargs):
        if self.request.method != 'GET':
            authentication_classes.append(TokenAuthentication)
        return authentication_classes

class ProducterViewSet(viewsets.ModelViewSet):
    queryset = Producter.objects.all()
    serializer_class = ProducterSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (AllowAny,)

    def get_authentication_classes(self, request, **kwargs):
        if self.request.method != 'GET':
            authentication_classes.append(TokenAuthentication)
        return authentication_classes

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProducterSerializer
        else:
            return ProducterListSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CommentSerializer
        else:
            return CommentListSerializer


class ExportCSVCars(APIView):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'
        writer = csv.writer(response)

        writer.writerow(['id', 'name', 'producter', 'start_year', 'last_year', 'comments', 'comments_count'])
        for row in Car.objects.all():
            writer.writerow([row.id, row.name, Producter.objects.filter(id=row.producter_id)[0], row.start_year, row.last_year,
                            list(Comment.objects.filter(car_id=row.id)),
                            Comment.objects.filter(car_id=row.id).count()])

        return response


class ExportCSVProducters(APIView):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'
        writer = csv.writer(response)

        writer.writerow(['id', 'name', 'country'])
        for row in Producter.objects.all():
            writer.writerow([row.id, row.name, Country.objects.filter(id=row.country_id)[0]])

        return response

class ExportCSVCountries(APIView):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'
        writer = csv.writer(response)

        writer.writerow(['id', 'name', 'producters'])
        for row in Country.objects.all():
            writer.writerow([row.id, row.name, list(Producter.objects.filter(country_id=row.id))])

        return response


class ExportCSVComments(APIView):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'
        writer = csv.writer(response)

        writer.writerow(['id', 'author_email', 'car', 'date_created', 'text'])
        for row in Comment.objects.all():
            writer.writerow([row.id, row.author_email, Car.objects.filter(id=row.car_id)[0], row.date_created, row.text])

        return response



