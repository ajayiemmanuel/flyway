# Generated by Django 4.2.3 on 2023-07-27 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0007_rename_profile_pic_product_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='img',
            new_name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
    ]