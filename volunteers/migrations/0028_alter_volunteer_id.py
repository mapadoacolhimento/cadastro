# Generated by Django 4.2.1 on 2023-11-28 14:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("volunteers", "0027_alter_volunteer_state"),
    ]

    operations = [
        migrations.AlterField(
            model_name="volunteer",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]