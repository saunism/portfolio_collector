# Generated by Django 3.0.5 on 2020-04-30 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0004_auto_20200430_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='sertificate',
            field=models.TextField(null=True),
        ),
    ]
