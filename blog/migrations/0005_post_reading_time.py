# Generated by Django 5.1.3 on 2024-12-11 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reading_time',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
