from django.core.exceptions import FieldDoesNotExist
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from vocabulary.models import Vocabulary


class VocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = (
            'title',
            'subtitle',
            'content',
            'starred',
        )


class VocabularyViewSet(ModelViewSet):
    serializer_class = VocabularySerializer
    permission_classes = AllowAny,
    lookup_field = 'title'
    keywords = 'starred',
    model = Vocabulary

    def get_queryset(self):
        self.validate_query_params()
        return self.model.objects.filter(
            **self.clean_query_params()
        )

    def clean_query_params(self):
        self.validate_keywords()
        return {
            key: value
            for key, value in self.request.query_params.items()
            if key in self.keywords
        }

    def validate_keywords(self):
        for keyword in self.keywords:
            if not hasattr(self.model(), keyword):
                raise FieldDoesNotExist(f'{keyword}필드가 존재하지 않습니다.')

    def validate_query_params(self):
        for field_name in self.keywords:
            self.validate_field(field_name)

    def validate_field(self, field_name):
        if field_name in self.request.query_params.keys():
            try:
                validator = getattr(self, f'validate_{field_name}')
            except AttributeError:
                raise NotImplementedError(f'validate_{field_name}를 구현해주세요.')
            validator(self.request.query_params[field_name])

    def validate_starred(self, value):
        if bool(value) not in (True, False):
            raise ValidationError()
