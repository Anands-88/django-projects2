# Generated by Django 3.1.13 on 2021-08-10 17:06

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contribution',
            old_name='parent',
            new_name='parents',
        ),
        migrations.RemoveField(
            model_name='contribution',
            name='Type',
        ),
        migrations.AddField(
            model_name='contribution',
            name='contributions',
            field=models.CharField(default='contr', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='parent',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='parent',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='parent',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
