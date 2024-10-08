# Generated by Django 3.2.21 on 2024-08-10 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField(default=18)),
                ('sex', models.CharField(max_length=20)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
