# Generated by Django 3.1.4 on 2020-12-24 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20201224_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='allergens',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='brand',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='ingredients',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='manufacturing_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity_type',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='item',
            name='remarks',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
