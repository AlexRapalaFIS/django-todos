# Generated by Django 4.2.5 on 2023-09-21 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('COMPLETED', 'Completed'), ('PENDING', 'Pending'), ('CANCELED', 'Canceled')], default='PENDING', max_length=128),
        ),
    ]
