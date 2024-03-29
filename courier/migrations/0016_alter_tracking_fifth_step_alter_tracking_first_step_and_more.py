# Generated by Django 4.2.3 on 2023-09-26 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0015_alter_product_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracking',
            name='fifth_step',
            field=models.CharField(default='Processing...', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='first_step',
            field=models.CharField(default='Processing...', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='fourth_step',
            field=models.CharField(default='Processing...', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='second_step',
            field=models.CharField(default='Processing...', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='sixth_step',
            field=models.CharField(default='Processing...', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='third_step',
            field=models.CharField(default='Processing...', max_length=200, null=True),
        ),
    ]
