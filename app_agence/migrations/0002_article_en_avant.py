# Generated by Django 5.1.2 on 2024-11-27 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_agence', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='en_avant',
            field=models.BooleanField(default=False),
        ),
    ]
