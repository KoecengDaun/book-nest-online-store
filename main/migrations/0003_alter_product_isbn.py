# Generated by Django 5.1.1 on 2024-10-06 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='isbn',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
