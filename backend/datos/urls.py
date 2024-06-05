from django.urls import path
from rest_framework import routers
from .api import MedidorViewSet, LoteoViewSet
from .views import reset_medidores_view

router = routers.DefaultRouter()

router.register('loteo', LoteoViewSet, 'loteo')
router.register('medidor', MedidorViewSet, 'medidor')

# Define las URLs para las vistas basadas en función
urlpatterns = [
    path('reset-medidores/', reset_medidores_view, name='reset-medidores'),
]

# Agregar las URLs generadas por el enrutador a las URLs definidas manualmente
urlpatterns += router.urls