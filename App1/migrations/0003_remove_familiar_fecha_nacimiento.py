# Generated by Django 4.1 on 2022-08-23 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_familiar_delete_curso_delete_entregable_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familiar',
            name='fecha_nacimiento',
        ),
    ]
