# Generated by Django 4.0.2 on 2022-02-13 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_contact_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.IntegerField(choices=[(1, 'Phone'), (2, 'Facebook'), (3, 'Email')]),
        ),
    ]
