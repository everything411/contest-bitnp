# Generated by Django 4.1.2 on 2022-10-30 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0006_draftresponse_deadline"),
    ]

    operations = [
        migrations.AlterField(
            model_name="draftresponse",
            name="student",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="quiz.student"
            ),
        ),
    ]
