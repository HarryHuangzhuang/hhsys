# Generated by Django 4.2.9 on 2024-02-25 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_article_category"),
    ]

    operations = [
        migrations.RenameField(
            model_name="article", old_name="Category", new_name="category",
        ),
        migrations.AddField(
            model_name="article",
            name="status",
            field=models.IntegerField(
                choices=[(1, "published"), (2, "delete")], default=1, verbose_name="状态"
            ),
        ),
    ]
