# Generated by Django 5.1.3 on 2024-12-11 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_reading_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='reading_time',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
