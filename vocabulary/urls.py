from rest_framework.routers import DefaultRouter

from vocabulary.views import VocabularyViewSet

router = DefaultRouter()
router.register(r'unit', VocabularyViewSet, basename='vocabulary')
