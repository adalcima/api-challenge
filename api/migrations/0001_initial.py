# Generated by Django 2.1.1 on 2020-08-05 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('value', models.FloatField()),
                ('discount_value', models.FloatField()),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
