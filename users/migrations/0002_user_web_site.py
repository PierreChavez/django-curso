# Generated by Django 5.0.6 on 2024-07-09 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='web_site',
            field=models.URLField(blank=True),
        ),
    ]