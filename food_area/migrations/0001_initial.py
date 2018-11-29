# Generated by Django 2.0.5 on 2018-11-29 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=100)),
                ('zip_code', models.PositiveSmallIntegerField()),
            ],
        ),
    ]