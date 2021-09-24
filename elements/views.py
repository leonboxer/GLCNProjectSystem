from rest_framework.viewsets import ModelViewSet

from .models import Element
from .serializers import ElementSerializer


class ElementViewSet(ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
    ordering_fields = ('id', 'tag', 'material')
    search_fields = ('tag', 'material')

    def get_queryset(self):
        queryset = Element.objects.all()
        tag = self.request.query_params.get('tag')
        if tag is not None:
            queryset = queryset.filter(tag=tag)
        return queryset
