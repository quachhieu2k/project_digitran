# Generated by Django 4.1 on 2022-09-06 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_recuitment", "0010_applyjob_cv_applyjob_pr"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employer",
            name="image",
            field=models.ImageField(
                blank=True, default=None, null=True, upload_to="images/"
            ),
        ),
    ]
