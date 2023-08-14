# Generated by Django 4.2.4 on 2023-08-14 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="department",
            fields=[
                (
                    "deptid",
                    models.CharField(
                        max_length=100, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("dept_name", models.CharField(max_length=100)),
                ("program", models.CharField(max_length=100)),
                ("School", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                ("Name", models.CharField(max_length=100)),
                (
                    "userid",
                    models.CharField(
                        max_length=100, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("year_of_joining", models.EmailField(max_length=254)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("AL", "Alumini"),
                            ("CR", "Current"),
                            ("FA", "Faculty"),
                        ],
                        default="CR",
                        max_length=100,
                    ),
                ),
                ("education_level", models.CharField(max_length=10)),
                ("about", models.TextField()),
                ("profile_photo", models.URLField()),
                (
                    "privacy",
                    models.CharField(
                        choices=[("PU", "Public"), ("PR", "Private")],
                        default="PU",
                        max_length=100,
                    ),
                ),
                ("phone_number", models.PositiveBigIntegerField()),
                ("linkedIn", models.URLField()),
                ("instagram", models.URLField()),
                ("skills", models.TextField()),
                ("interests", models.TextField()),
                (
                    "deptid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="network.department",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Users",
            fields=[
                (
                    "profile",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="network.profile",
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Posts",
            fields=[
                (
                    "postid",
                    models.CharField(
                        max_length=100, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("caption", models.CharField(max_length=250)),
                ("tags", models.CharField(max_length=250)),
                ("image_or_video", models.URLField()),
                (
                    "userid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="network.profile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Likes",
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
                (
                    "postid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="network.posts"
                    ),
                ),
                (
                    "userid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="network.profile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Following",
            fields=[
                (
                    "followingid",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("date_followed", models.DateField()),
                (
                    "request_status",
                    models.CharField(
                        choices=[("PE", "Pending"), ("AC", "Accepted")], max_length=100
                    ),
                ),
                (
                    "userid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="network.profile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Feedback",
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
                ("feedback", models.TextField()),
                (
                    "userid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="network.profile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comments",
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
                ("comments", models.TextField()),
                (
                    "postid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="network.posts"
                    ),
                ),
                (
                    "userid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="network.profile",
                    ),
                ),
            ],
        ),
    ]
