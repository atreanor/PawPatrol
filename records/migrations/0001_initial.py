# Generated by Django 2.0.6 on 2018-11-02 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
                ('amountLeftOver', models.IntegerField()),
                ('amountDispensed', models.IntegerField()),
                ('additionalInfo', models.TextField()),
            ],
        ),
    ]
