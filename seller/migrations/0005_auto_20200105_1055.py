# Generated by Django 2.1 on 2020-01-05 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_auto_20200105_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='describe',
            field=models.TextField(max_length=500),
        ),
    ]