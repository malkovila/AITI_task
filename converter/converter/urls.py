from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CurrencyViewSet

router = DefaultRouter()
router.register(r'api', CurrencyViewSet, basename='currency')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
