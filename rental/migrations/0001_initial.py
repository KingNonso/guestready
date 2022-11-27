# Generated by Django 4.1.3 on 2022-11-27 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Rental",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Reservation",
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
                ("rental_id", models.CharField(max_length=100)),
                ("checkin", models.DateField()),
                ("checkout", models.DateField()),
                (
                    "rent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="rental.rental"
                    ),
                ),
            ],
            options={
                "ordering": ["rental_id"],
            },
        ),
        migrations.AddConstraint(
            model_name="reservation",
            constraint=models.CheckConstraint(
                check=models.Q(("checkin__lte", models.F("checkout"))),
                name="checkin_lte_checkout",
            ),
        ),
    ]
