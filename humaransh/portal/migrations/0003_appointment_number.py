# Generated by Django 4.0.2 on 2022-02-02 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='number',
            field=models.CharField(default=2, max_length=10),
            preserve_default=False,
        ),
    ]