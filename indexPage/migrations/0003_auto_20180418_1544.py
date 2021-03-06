# Generated by Django 2.0.4 on 2018-04-18 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexPage', '0002_auto_20180417_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='id',
        ),
        migrations.AlterField(
            model_name='account',
            name='account_tel',
            field=models.CharField(max_length=128, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='nickname',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='hr',
            name='convert_num',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='hr',
            name='download_num',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='hr',
            name='gift_value',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='hr',
            name='share_num',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='hr',
            name='viedeo_src',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
