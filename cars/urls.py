from django.contrib import admin
from django.contrib.auth import login
from django.urls import path, include, re_path
from talk.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'cars', CarViewSet)

router2 = routers.SimpleRouter()
router2.register(r'producters', ProducterViewSet)

router3 = routers.SimpleRouter()
router3.register(r'countries', CountryViewSet)

router4 = routers.SimpleRouter()
router4.register(r'comments', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include(router2.urls)),
    path('api/', include(router3.urls)),
    path('api/', include(router4.urls)),
    path('api/report/producters', ExportCSVProducters.as_view(),
         ),
    path('api/report/cars', ExportCSVCars.as_view(),
         ),
    path('api/report/countries', ExportCSVCountries.as_view(),
         ),
    path('api/report/comments', ExportCSVComments.as_view(),
         ),
    path('api/drf-auth/', include('rest_framework.urls')),
    path('api/auth/', include('djoser.urls')),
    re_path(r'auth/', include('djoser.urls.authtoken')),


]
