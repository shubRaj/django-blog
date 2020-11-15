# Generated by Django 3.1.2 on 2020-11-15 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-created_on'], 'verbose_name': 'Blog'},
        ),
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(default='gell', unique=True),
        ),
    ]
