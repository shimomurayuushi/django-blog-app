# Generated by Django 4.0.2 on 2023-05-23 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'カテゴリー', 'verbose_name_plural': 'カテゴリー'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': '記事', 'verbose_name_plural': '記事'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'タグ', 'verbose_name_plural': 'タグ'},
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名前')),
                ('text', models.TextField(verbose_name='本文')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='記事')),
            ],
            options={
                'verbose_name': 'コメント',
                'verbose_name_plural': 'コメント',
            },
        ),
    ]
