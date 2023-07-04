# Generated by Django 3.0.6 on 2020-05-31 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Teacher id')),
                ('started_at', models.DateField(verbose_name='Started at')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Teacher',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Student id')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Student',
            },
        ),
    ]
