# Generated by Django 4.0.6 on 2022-07-24 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_customuser_specialization'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provinces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('code', models.CharField(blank=True, max_length=5, null=True)),
            ],
        ),
    ]