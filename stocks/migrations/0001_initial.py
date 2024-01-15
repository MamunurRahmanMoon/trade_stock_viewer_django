# Generated by Django 4.2.5 on 2024-01-13 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('trade_code', models.CharField(max_length=50)),
                ('high', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('low', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('open', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('close', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('volume', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
