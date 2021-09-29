from rest_framework.routers import DefaultRouter

from vocabulary.views import VocabularyViewSet

router = DefaultRouter()
router.register(r'vocabulary', VocabularyViewSet, basename='vocabulary')
urlpatterns = router.urls
