# Generated by Django 3.1.1 on 2021-07-26 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0006_auto_20210726_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Blog Post', max_length=255),
        ),
    ]