# Generated by Django 3.0.14 on 2024-04-24 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='name_product',
        ),
    ]
