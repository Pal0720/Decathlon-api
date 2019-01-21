# Generated by Django 2.1.4 on 2019-01-19 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=128)),
                ('product_sport', models.CharField(max_length=128)),
                ('product_level', models.IntegerField()),
                ('product_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('store_id', models.AutoField(primary_key=True, serialize=False)),
                ('store_name', models.CharField(max_length=64)),
                ('store_city', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='associated_stores',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.Stores'),
        ),
    ]
