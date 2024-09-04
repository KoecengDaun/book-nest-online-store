# Generated by Django 5.1.1 on 2024-09-04 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=100)),
                ('publication_year', models.IntegerField()),
                ('stock', models.IntegerField(default=0)),
                ('isbn', models.CharField(blank=True, max_length=13, null=True, unique=True)),
            ],
        ),
    ]