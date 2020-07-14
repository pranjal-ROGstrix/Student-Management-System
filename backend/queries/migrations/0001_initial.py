# Generated by Django 2.0 on 2020-07-14 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0003_student_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='queries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=250)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='active', max_length=10)),
                ('key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.student')),
            ],
        ),
    ]
