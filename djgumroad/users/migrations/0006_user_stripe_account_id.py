# Generated by Django 3.0.11 on 2021-02-04 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210203_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stripe_account_id',
            field=models.CharField(default='123', max_length=100),
            preserve_default=False,
        ),
    ]
