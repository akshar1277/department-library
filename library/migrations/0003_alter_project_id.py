# Generated by Django 3.2.9 on 2022-10-05 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_project_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
