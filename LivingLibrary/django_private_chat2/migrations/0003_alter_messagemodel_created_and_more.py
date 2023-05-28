# Generated by Django 4.2.1 on 2023-05-28 22:14

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_private_chat2', '0002_alter_messagemodel_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagemodel',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='messagemodel',
            name='is_removed',
            field=models.BooleanField(default=False),
        ),
    ]
