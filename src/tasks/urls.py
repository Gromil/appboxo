
from rest_framework.routers import DefaultRouter

from tasks.views import CategoryViewSet, TaskViewSet

router = DefaultRouter()

router.register('tasks', TaskViewSet)
router.register('category', CategoryViewSet)

urlpatterns = router.urls
