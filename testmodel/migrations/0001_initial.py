# Generated by Django 2.2.17 on 2021-06-10 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('name', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('memtest', models.CharField(max_length=32)),
                ('homo_linpack', models.CharField(max_length=32)),
                ('heter_linpack', models.CharField(max_length=32)),
                ('heter_dgemm', models.CharField(max_length=32)),
                ('heter_stream', models.CharField(max_length=32)),
                ('change_time', models.DateTimeField()),
            ],
        ),
    ]
