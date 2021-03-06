# Generated by Django 2.1 on 2020-01-05 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0005_auto_20200105_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preferential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferential_type', models.IntegerField()),
                ('enoughNumber', models.FloatField()),
                ('minusNumber', models.FloatField()),
                ('discount', models.FloatField()),
                ('cutOffDatetime', models.DateField()),
                ('describe', models.TextField(max_length=500)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='isPreferential',
            field=models.CharField(default='否', max_length=1),
        ),
        migrations.AddField(
            model_name='preferential',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='seller.Goods'),
        ),
        migrations.AddField(
            model_name='preferential',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='seller.Seller'),
        ),
        migrations.AlterIndexTogether(
            name='preferential',
            index_together={('id',)},
        ),
    ]
