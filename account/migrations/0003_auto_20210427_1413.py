# Generated by Django 2.2.13 on 2021-04-27 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210426_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.CharField(choices=[('admin', 'admin'), ('editor', 'editor')], default='admin', max_length=10),
        ),
    ]