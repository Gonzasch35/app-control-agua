from rest_framework import routers
from .api import MedidorViewSet, LoteoViewSet

router = routers.DefaultRouter()

router.register('loteo', LoteoViewSet, 'loteo')
router.register('medidor', MedidorViewSet, 'medidor')

urlpatterns = router.urls