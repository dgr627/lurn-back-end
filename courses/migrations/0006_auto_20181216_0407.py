# Generated by Django 2.0.7 on 2018-12-16 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20181216_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercard',
            name='score',
            field=models.FloatField(null=True),
        ),
    ]
