# Generated by Django 5.0.1 on 2024-02-06 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'Цветы', 'verbose_name_plural': 'Цветы'},
        ),
    ]