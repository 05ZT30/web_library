# Generated by Django 3.2.15 on 2023-01-13 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_myuser_card_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
