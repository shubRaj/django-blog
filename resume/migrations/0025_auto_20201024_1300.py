# Generated by Django 3.1.2 on 2020-10-24 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0024_auto_20201024_0420'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favicon_pic',
            field=models.ImageField(default='profile_pics/favicondefault.png', upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='profile',
            name='resume_pic',
            field=models.ImageField(default='profile_pics/default.png', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='profile_pics/profiledefault.png', upload_to='profile_pics'),
        ),
    ]
