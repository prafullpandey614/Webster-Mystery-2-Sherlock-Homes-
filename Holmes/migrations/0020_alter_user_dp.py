# Generated by Django 4.1.6 on 2023-02-10 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Holmes", "0019_alter_user_dp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="dp",
            field=models.ImageField(default="media/th_19.jfif", upload_to="media"),
        ),
    ]
