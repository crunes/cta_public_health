# Generated by Django 2.0.2 on 2020-03-04 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='questions',
            new_name='question',
        ),
    ]
