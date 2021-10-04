from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from vocabulary.models import Vocabulary


class VocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = (
            'title',
            'subtitle',
            'modified_datetime',
            'searched_datetime',
            'content',
        )


class VocabularyViewSet(ModelViewSet):
    serializer_class = VocabularySerializer
    permission_classes = AllowAny,
    queryset = Vocabulary.objects.all()
    lookup_field = 'title'
