from rest_framework import routers
from .api import RecipeViewSet

router = routers.DefaultRouter()
router.register('api/recipies', RecipeViewSet, 'recipies')

urlpatterns = router.urls
