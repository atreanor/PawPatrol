# Generated by Django 2.1.3 on 2018-11-22 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0017_auto_20181122_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='additionalInfo',
            field=models.TextField(default='-'),
        ),
    ]
