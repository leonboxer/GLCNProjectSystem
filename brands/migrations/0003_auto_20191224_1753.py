# Generated by Django 3.0 on 2019-12-24 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0002_auto_20191206_1024'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'ordering': ('brand_name',)},
        ),
        migrations.RenameField(
            model_name='brand',
            old_name='created_time',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='brand',
            old_name='update_time',
            new_name='updated',
        ),
    ]
