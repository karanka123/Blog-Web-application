# Generated by Django 5.0 on 2023-12-26 06:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Login", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="blog",
            old_name="author",
            new_name="Author",
        ),
        migrations.RenameField(
            model_name="blog",
            old_name="content",
            new_name="Content",
        ),
        migrations.RenameField(
            model_name="blog",
            old_name="image",
            new_name="Image",
        ),
        migrations.RenameField(
            model_name="blog",
            old_name="title",
            new_name="Title",
        ),
    ]