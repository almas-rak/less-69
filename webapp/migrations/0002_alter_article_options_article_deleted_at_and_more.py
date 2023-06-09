# Generated by Django 4.1.6 on 2023-02-28 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="article",
            options={"verbose_name": "Статья", "verbose_name_plural": "Статьи"},
        ),
        migrations.AddField(
            model_name="article",
            name="deleted_at",
            field=models.DateTimeField(
                default=None, null=True, verbose_name="Дата и время удаления"
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="is_deleted",
            field=models.BooleanField(default=False, verbose_name="удалено"),
        ),
        migrations.AddField(
            model_name="article",
            name="status",
            field=models.CharField(
                choices=[("ACTIVE", "Активна"), ("NOT_ACTIVE", "Неактивна")],
                default="ACTIVE",
                max_length=20,
                verbose_name="Статус",
            ),
        ),
    ]
