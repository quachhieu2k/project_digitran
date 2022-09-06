# Generated by Django 4.1 on 2022-08-30 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_recuitment", "0008_alter_job_company"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="type",
            field=models.CharField(
                choices=[
                    ("Full time", "Full time"),
                    ("Part time", "Part time"),
                    ("Internship", "Internship"),
                ],
                max_length=10,
            ),
        ),
    ]