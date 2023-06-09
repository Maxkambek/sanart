# Generated by Django 4.2.1 on 2023-06-01 12:58

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=223)),
                ('name_uz', models.CharField(max_length=223, null=True)),
                ('name_en', models.CharField(max_length=223, null=True)),
                ('name_ru', models.CharField(max_length=223, null=True)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=450)),
                ('name_uz', models.CharField(max_length=450, null=True)),
                ('name_en', models.CharField(max_length=450, null=True)),
                ('name_ru', models.CharField(max_length=450, null=True)),
                ('sort_number', models.PositiveIntegerField(unique=True)),
                ('views', models.PositiveIntegerField(default=1)),
                ('deadline', models.DateTimeField()),
                ('start_price', models.PositiveIntegerField()),
                ('trade_type', models.CharField(choices=[('Auction', 'Action'), ('Sale', 'Sale')], max_length=100)),
                ('trade_style', models.CharField(choices=[('Increase', 'Increase'), ('OneTime', 'OneTime')], max_length=100)),
                ('start_date', models.DateTimeField()),
                ('back_price', models.CharField(max_length=123)),
                ('first_step_percent', models.PositiveIntegerField(default=10)),
                ('address', models.CharField(max_length=300)),
                ('address_uz', models.CharField(max_length=300, null=True)),
                ('address_en', models.CharField(max_length=300, null=True)),
                ('address_ru', models.CharField(max_length=300, null=True)),
                ('description', models.TextField()),
                ('description_uz', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(choices=[('New', 'New'), ('Waiting', 'Waiting'), ('Send', 'Send'), ('Ordered', 'Ordered')], max_length=123)),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.catalog')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_images', to='main.property')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/')),
                ('obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_files', to='main.property')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField()),
                ('text_uz', ckeditor.fields.RichTextField(null=True)),
                ('text_en', ckeditor.fields.RichTextField(null=True)),
                ('text_ru', ckeditor.fields.RichTextField(null=True)),
                ('obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_details', to='main.property')),
            ],
        ),
    ]
