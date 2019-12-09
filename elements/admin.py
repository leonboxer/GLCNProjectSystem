from django.contrib import admin
from .models import Element
from materials.models import Material
from tags.models import Tag
from import_export.admin import ImportExportModelAdmin
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget


class ElementResource(resources.ModelResource):
    material = fields.Field(
        column_name='Order No.',
        attribute='element_material',
        widget=ForeignKeyWidget(Material, 'order_number')
    )
    tag = fields.Field(
        column_name='Tag No.',
        attribute='element_tag',
        widget=ForeignKeyWidget(Tag, 'tag_number')
    )

    class Meta:
        model = Element
        exclude = ('id', 'element_material', 'element_tag')


# Register your models here.
@admin.register(Element)
class ElementAdmin(ImportExportModelAdmin):
    resource_class = ElementResource
    list_display = ['element_tag', 'element_material']
    list_filter = ['element_tag', 'element_material']
    autocomplete_fields = ['element_tag', 'element_material']
    search_fields = ['element_tag', 'element_material']
