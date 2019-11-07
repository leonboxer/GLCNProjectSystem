from import_export import resources
from .models import Tag


class TagResource(resources.ModelResource):
    class Meta:
        model = Tag
        exclude = ('id',)
        import_id_fields = ['tag_number']
        # fields = ('brand')
