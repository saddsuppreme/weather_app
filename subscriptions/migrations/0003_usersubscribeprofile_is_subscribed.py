# Generated by Django 4.0.5 on 2022-06-21 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_alter_usersubscribeprofile_sub_expiration_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersubscribeprofile',
            name='is_subscribed',
            field=models.BooleanField(default=False),
        ),
    ]
