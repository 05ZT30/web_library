# Generated by Django 3.2.15 on 2023-01-05 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_alter_person_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
