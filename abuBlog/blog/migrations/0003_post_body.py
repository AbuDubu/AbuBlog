# Generated by Django 4.0.4 on 2022-05-05 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_delete_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default='this is the body'),
            preserve_default=False,
        ),
    ]
