# Generated by Django 4.1.2 on 2022-10-30 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0002_choice_question_student_response_draftresponse_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="name",
            field=models.CharField(default="侯瀚茗", max_length=50),
            preserve_default=False,
        ),
    ]
