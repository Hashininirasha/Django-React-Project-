# Generated by Django 4.2.6 on 2023-10-17 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0011_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment_Areas',
            fields=[
                ('Assessment_Areas_Id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Assessment_Area', models.CharField(max_length=200)),
            ],
        ),
    ]
