# Generated by Django 2.0.5 on 2019-01-24 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_order', '0003_auto_20190124_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='client_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_users_profile.Profile'),
        ),
    ]