# Generated by Django 3.2.21 on 2024-08-31 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_personmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('age', models.IntegerField(default=18)),
            ],
            options={
                'db_table': 'person',
            },
        ),
    ]
