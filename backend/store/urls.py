from rest_framework.routers import DefaultRouter

from store import views


router = DefaultRouter()
router.register("products", views.ProductViewSet)
router.register("category", views.CategoryViewSet)
router.register("store", views.StoreViewSet)

urlpatterns = router.urls
