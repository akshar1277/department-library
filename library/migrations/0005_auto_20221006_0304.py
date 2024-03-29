# Generated by Django 3.2.9 on 2022-10-05 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_alter_project_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_second',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('Batch', models.CharField(max_length=10, null=True)),
                ('Project_id', models.CharField(max_length=15, null=True)),
                ('Project_type', models.CharField(choices=[('UDP', 'UDP'), ('IDP', 'IDP')], default='UDP', max_length=20, null=True)),
                ('Project_name', models.CharField(max_length=100, null=True)),
                ('Abstract', models.CharField(max_length=500, null=True)),
                ('Project_area', models.CharField(max_length=200, null=True)),
                ('Langauge', models.CharField(max_length=100, null=True)),
                ('Company_name', models.CharField(max_length=100, null=True)),
                ('Leader_enroll', models.IntegerField(null=True)),
                ('Leader_name', models.CharField(max_length=50, null=True)),
                ('Leader_email', models.EmailField(max_length=254, null=True)),
                ('Internal_guide', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Projects_2020-21',
                'verbose_name_plural': 'Projects_2020-21',
            },
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Projects_2019-20', 'verbose_name_plural': 'Projects_2019-20'},
        ),
    ]
