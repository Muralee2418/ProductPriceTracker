# Generated by Django 3.2.5 on 2022-02-03 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemUrl', models.URLField(max_length=1000)),
                ('itemName', models.CharField(max_length=100)),
                ('itemPrice', models.BigIntegerField()),
                ('itemImage', models.CharField(max_length=500)),
                ('itemDescription', models.TextField()),
                ('itemDate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
