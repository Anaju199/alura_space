# Generated by Django 5.0.1 on 2024-01-18 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("galeria", "0002_fotografia_categoria"),
    ]

    operations = [
        migrations.AddField(
            model_name="fotografia",
            name="publicada",
            field=models.BooleanField(default=False),
        ),
    ]
