# Generated by Django 4.0.5 on 2022-07-06 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visit',
            old_name='Visit_lenght',
            new_name='Visit_length',
        ),
        migrations.AddField(
            model_name='visit',
            name='Day',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='visit',
            name='Term',
            field=models.TimeField(null=True),
        ),
    ]
