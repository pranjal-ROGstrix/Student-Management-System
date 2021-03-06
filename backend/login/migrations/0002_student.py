# Generated by Django 2.0 on 2020-07-14 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('father_name', models.CharField(max_length=20)),
                ('lib_id', models.CharField(max_length=10, unique=True)),
                ('course', models.CharField(max_length=10)),
                ('mobile_no', models.CharField(max_length=10, unique=True)),
                ('branch', models.CharField(max_length=10)),
                ('sec', models.CharField(max_length=5)),
                ('status', models.CharField(default='active', max_length=15)),
                ('email', models.CharField(max_length=30, unique=True)),
            ],
        ),
    ]
