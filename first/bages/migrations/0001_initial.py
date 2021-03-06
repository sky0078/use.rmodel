# Generated by Django 3.2.9 on 2021-11-24 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True)),
                ('active', models.BooleanField(default=False)),
                ('date', models.DateTimeField(null=True)),
                ('sms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bages.message')),
            ],
        ),
    ]
