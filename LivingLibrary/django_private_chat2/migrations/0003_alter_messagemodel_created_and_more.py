<<<<<<< HEAD
# Generated by Django 4.2.1 on 2023-05-22 09:59

from django.db import migrations, models
=======
# Generated by Django 4.2.1 on 2023-05-28 22:14

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
>>>>>>> master


class Migration(migrations.Migration):

    dependencies = [
<<<<<<< HEAD
        ('django_private_chat2', '0002_alter_messagemodel_is_removed'),
=======
        ('django_private_chat2', '0002_alter_messagemodel_created_and_more'),
>>>>>>> master
    ]

    operations = [
        migrations.AlterField(
            model_name='messagemodel',
            name='created',
<<<<<<< HEAD
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='messagemodel',
            name='modified',
            field=models.DateTimeField(auto_now_add=True, verbose_name='修改时间'),
=======
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='messagemodel',
            name='is_removed',
            field=models.BooleanField(default=False),
>>>>>>> master
        ),
    ]
