# Generated by Django 2.1.11 on 2020-03-15 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20200304_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='暂无', max_length=100),
        ),
    ]
