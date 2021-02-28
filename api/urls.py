from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'categories', views.CategoryViewSet)
# router.register(r'disease/(?P<name>.+)', views.DiseaseList, basename='disease')

urlpatterns = [
    path('api/', include((router.urls, 'products'), namespace='api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('postman/', views.api, name='api'),
    path('traffic/', views.traffic, name='traffic')
]
