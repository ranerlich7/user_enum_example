# Generated by Django 5.1.2 on 2024-11-01 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskuser',
            name='user_type',
            field=models.CharField(choices=[('DR', 'Driver'), ('PA', 'Passenger')], default='PA', max_length=2),
        ),
    ]
