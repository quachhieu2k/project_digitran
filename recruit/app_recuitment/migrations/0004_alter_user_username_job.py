# Generated by Django 4.1 on 2022-08-29 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app_recuitment", "0003_employee"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.CreateModel(
            name="Job",
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
                ("name", models.CharField(blank=True, max_length=45, null=True)),
                ("desc", models.TextField(blank=True, null=True)),
                ("requirements", models.TextField(blank=True, null=True)),
                ("benefits", models.TextField(blank=True, null=True)),
                ("number_req", models.IntegerField(blank=True, null=True)),
                ("status", models.CharField(blank=True, max_length=2, null=True)),
                ("deadline", models.DateField(blank=True, null=True)),
                ("create_at", models.DateTimeField(blank=True, null=True)),
                ("publish_date", models.DateField(blank=True, null=True)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="app_recuitment.employer",
                    ),
                ),
            ],
        ),
    ]
