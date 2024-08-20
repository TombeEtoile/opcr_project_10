from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api.urls import router as api_router


router = routers.DefaultRouter()
router.registry.extend(api_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
