# Generated by Django 4.0.6 on 2022-07-13 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instaworkapp', '0004_alter_adddata_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adddata',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
