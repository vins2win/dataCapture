# Generated by Django 3.1.4 on 2020-12-23 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('barcode', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity_type', models.CharField(blank=True, max_length=32)),
                ('manufacturer', models.CharField(blank=True, max_length=64)),
                ('brand', models.CharField(blank=True, max_length=64)),
                ('manufacturing_date', models.DateField(blank=True)),
                ('expirey_date', models.DateField(blank=True)),
                ('ingredients', models.CharField(blank=True, max_length=128)),
                ('allergens', models.CharField(blank=True, max_length=64)),
                ('remarks', models.CharField(blank=True, max_length=128)),
                ('images', models.JSONField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.itemcategory')),
                ('shop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.shop')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.user')),
            ],
        ),
    ]