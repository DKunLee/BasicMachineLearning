# Generated by Django 5.1.3 on 2024-11-16 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0005_alter_post_thumbnail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="thumbnail",
            field=models.ImageField(upload_to="post/"),
        ),
    ]
