# Generated by Django 4.1 on 2022-08-29 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app_recuitment", "0004_alter_user_username_job"),
    ]

    operations = [
        migrations.RenameField(model_name="job", old_name="name", new_name="title",),
        migrations.RemoveField(model_name="job", name="create_at",),
        migrations.RemoveField(model_name="job", name="publish_date",),
        migrations.RemoveField(model_name="job", name="status",),
        migrations.CreateModel(
            name="Education",
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
                ("college", models.CharField(blank=True, max_length=200, null=True)),
                ("address", models.CharField(blank=True, max_length=45, null=True)),
                ("major", models.CharField(blank=True, max_length=45, null=True)),
                ("start_year", models.DateField(blank=True, null=True)),
                ("grad_year", models.DateField(blank=True, null=True)),
                (
                    "gpa",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=4, null=True
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="app_recuitment.employee",
                    ),
                ),
            ],
        ),
    ]
