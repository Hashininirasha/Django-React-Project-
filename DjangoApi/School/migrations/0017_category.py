# Generated by Django 4.2.6 on 2023-10-18 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0016_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('Category_Id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Category', models.CharField(max_length=200)),
            ],
        ),
    ]