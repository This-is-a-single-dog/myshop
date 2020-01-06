# Generated by Django 2.1 on 2020-01-04 08:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=11)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=255)),
                ('registerDate', models.DateField(default=django.utils.timezone.now)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.AlterIndexTogether(
            name='seller',
            index_together={('id', 'name', 'email')},
        ),
    ]
