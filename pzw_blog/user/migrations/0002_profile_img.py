# Generated by Django 2.1.11 on 2020-03-15 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, upload_to='img/%Y/%m'),
        ),
    ]