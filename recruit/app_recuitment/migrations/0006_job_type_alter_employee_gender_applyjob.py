# Generated by Django 4.1 on 2022-08-29 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("app_recuitment", "0005_rename_name_job_title_remove_job_create_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="type",
            field=models.CharField(
                choices=[("1", "Full time"), ("2", "Part time"), ("3", "Internship")],
                default=11,
                max_length=10,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="employee",
            name="gender",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.CreateModel(
            name="Applyjob",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applicants",
                        to="app_recuitment.job",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]