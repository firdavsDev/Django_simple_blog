# Generated by Django 3.2.4 on 2021-06-03 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210603_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sale',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
