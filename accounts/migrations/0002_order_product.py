# Generated by Django 4.1.1 on 2022-09-24 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out for deliverly', 'Out for deliverly'), ('Deliverly', 'Deliverly')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=b'I01\n')),
                ('category', models.CharField(choices=[('New', 'New'), ('Old', 'Old')], max_length=200, null=True)),
                ('descrption', models.CharField(max_length=200, null=True)),
                ('datecreated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
