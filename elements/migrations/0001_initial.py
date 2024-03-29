# Generated by Django 3.2.3 on 2021-05-26 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='elements', to='materials.material')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='elements', to='tags.tag')),
            ],
        ),
    ]
