# Generated by Django 4.0.2 on 2023-05-18 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_tag_alter_category_slug_alter_post_category_post_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tag',
            new_name='tags',
        ),
    ]
