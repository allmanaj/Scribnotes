# Generated by Django 2.1.7 on 2019-04-10 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0016_auto_20190410_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classnote',
            name='title',
            field=models.CharField(max_length=47),
        ),
    ]