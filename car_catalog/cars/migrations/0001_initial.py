# Generated by Django 4.2.7 on 2023-11-25 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='car_images/')),
                ('link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]