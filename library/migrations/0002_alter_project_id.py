# Generated by Django 3.2.9 on 2022-10-05 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
