# Generated by Django 2.2.17 on 2021-06-10 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testmodel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='change_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
