# Generated by Django 4.1.6 on 2023-02-10 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Holmes", "0011_alter_jobs_skills"),
    ]

    operations = [
        migrations.AlterField(
            model_name="skill",
            name="name",
            field=models.CharField(max_length=40),
        ),
    ]