# Generated by Django 4.1 on 2022-08-30 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app_recuitment", "0007_alter_job_company"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="company",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="jobbs",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
