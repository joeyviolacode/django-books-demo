# Generated by Django 4.0.5 on 2022-06-11 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
