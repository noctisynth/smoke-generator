# Generated by Django 5.0.6 on 2024-05-13 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smoke', '0003_alter_jointrecord_options_alter_smokerecord_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jointrecord',
            name='url',
            field=models.CharField(max_length=273, verbose_name='图片地址'),
        ),
        migrations.AlterField(
            model_name='smokerecord',
            name='url',
            field=models.CharField(max_length=273, verbose_name='图片地址'),
        ),
    ]
