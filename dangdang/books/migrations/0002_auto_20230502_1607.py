# Generated by Django 3.2.6 on 2023-05-02 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='author',
        ),
        migrations.RemoveField(
            model_name='books',
            name='press',
        ),
        migrations.RemoveField(
            model_name='press',
            name='author',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Books',
        ),
        migrations.DeleteModel(
            name='Press',
        ),
    ]
