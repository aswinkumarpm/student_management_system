# Generated by Django 3.2.8 on 2021-10-09 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20211009_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmark',
            name='total_mark',
            field=models.IntegerField(default=0),
        ),
    ]
