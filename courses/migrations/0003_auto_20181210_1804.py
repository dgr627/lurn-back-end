# Generated by Django 2.0.7 on 2018-12-10 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20181126_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='lesson_course',
            field=models.CharField(default='none', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lesson',
            name='lesson_level',
            field=models.IntegerField(choices=[(1, 'Introductory'), (2, 'Basic'), (3, 'Medium'), (4, 'Hard'), (5, 'Expert')], default=3),
            preserve_default=False,
        ),
    ]
