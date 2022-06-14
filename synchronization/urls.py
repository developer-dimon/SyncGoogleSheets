from django.urls import path
from rest_framework.routers import DefaultRouter

from synchronization.api.views import OrderViewSet, update_data

router = DefaultRouter()
router.register('api/orders', OrderViewSet, basename='orders')
urlpatterns = router.urls
urlpatterns += [
    path('update-data/', update_data)
]
