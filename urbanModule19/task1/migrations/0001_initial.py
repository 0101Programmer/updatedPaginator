# Generated by Django 5.1.1 on 2024-10-06 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default=None)),
                ('balance', models.DecimalField(decimal_places=10, default=0, max_digits=19)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default=None)),
                ('cost', models.DecimalField(decimal_places=10, default=None, max_digits=19)),
                ('size', models.DecimalField(decimal_places=10, default=None, max_digits=19)),
                ('description', models.TextField(default=None)),
                ('age_limited', models.BooleanField(default=False)),
                ('buyer', models.ManyToManyField(related_name='games', to='task1.buyer')),
            ],
        ),
    ]
