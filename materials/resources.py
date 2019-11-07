from import_export import resources
from .models import Material


class MaterialResource(resources.ModelResource):
    class Meta:
        model = Material
        # import_id_fields = ('order_number',)
        fields = ('order_number', 'type', 'brand')
