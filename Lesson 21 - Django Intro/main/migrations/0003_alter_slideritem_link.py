# Generated by Django 4.2.2 on 2023-06-16 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_slideritem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slideritem',
            name='link',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
