# Generated by Django 5.1.1 on 2024-10-07 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paginatorapp', '0004_alter_pages_number_of_posts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pages',
            new_name='SavedPostNums',
        ),
    ]
