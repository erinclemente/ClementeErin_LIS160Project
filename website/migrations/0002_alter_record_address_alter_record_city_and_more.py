# Generated by Django 5.1.3 on 2024-12-18 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='address',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='record',
            name='city',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='record',
            name='phone',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='record',
            name='state',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='record',
            name='zipcode',
            field=models.CharField(max_length=1000),
        ),
    ]
