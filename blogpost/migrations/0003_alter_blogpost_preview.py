# Generated by Django 4.2.2 on 2024-06-02 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogpost", "0002_alter_blogpost_options_alter_blogpost_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="preview",
            field=models.ImageField(blank=True, null=True, upload_to="blogpost/"),
        ),
    ]