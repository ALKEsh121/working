# Generated by Django 5.0.4 on 2024-05-30 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tezcoapp', '0003_alter_contact_name_alter_enquiry_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
