# Generated by Django 2.1.3 on 2018-11-22 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0016_auto_20181122_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='additionalInfo',
            field=models.TextField(default=' '),
        ),
    ]
