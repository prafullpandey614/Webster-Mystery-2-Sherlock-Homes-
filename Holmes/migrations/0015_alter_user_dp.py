# Generated by Django 4.1.6 on 2023-02-10 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Holmes", "0014_remove_user_jobs_applied_user_jobs_applied"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="dp",
            field=models.ImageField(
                blank=True, default="media/th_19.jfif", null=True, upload_to="media"
            ),
        ),
    ]