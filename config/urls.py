from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api.views import EstadoViewSet, CartoriosViewSet, CartorioUfList

router = routers.DefaultRouter()
router.register('estado', EstadoViewSet)
router.register('cartorios', CartoriosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
