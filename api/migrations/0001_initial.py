# Generated by Django 4.2.5 on 2023-09-21 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=128)),
                ('status', models.CharField(choices=[('COMPLETED', 'Completed'), ('PENDING', 'Pending'), ('CANCELED', 'Canceled')], max_length=128)),
            ],
        ),
    ]