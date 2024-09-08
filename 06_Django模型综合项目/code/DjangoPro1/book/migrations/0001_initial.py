# Generated by Django 3.2.21 on 2024-09-08 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('publisher', '0001_initial'),
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='书名')),
                ('publish_date', models.DateField(verbose_name='出版时间')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author.author', verbose_name='作者')),
                ('publishers', models.ManyToManyField(to='publisher.Publisher', verbose_name='出版社')),
            ],
        ),
    ]
