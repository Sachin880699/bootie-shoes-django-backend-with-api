# Generated by Django 3.2.10 on 2022-01-01 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('email', models.CharField(blank=True, max_length=1000, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=1000, null=True)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SellingItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='selling_item_image')),
                ('rating', models.CharField(blank=True, max_length=1000, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('mobile', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
