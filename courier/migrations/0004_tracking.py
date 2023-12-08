# Generated by Django 4.2.3 on 2023-07-26 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courier', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_step', models.CharField(max_length=200, null=True)),
                ('second_step', models.CharField(max_length=200, null=True)),
                ('third_step', models.CharField(max_length=200, null=True)),
                ('fourth_step', models.CharField(max_length=200, null=True)),
                ('fifth_step', models.CharField(max_length=200, null=True)),
                ('sixth_step', models.CharField(max_length=200, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]