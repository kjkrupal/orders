from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register("create", views.OrderViewset, basename="create_orders")

urlpatterns = router.urls