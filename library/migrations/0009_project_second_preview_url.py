# Generated by Django 3.2.9 on 2022-12-27 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_project_preview_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_second',
            name='Preview_URL',
            field=models.URLField(null=True),
        ),
    ]
