# Generated by Django 5.0.4 on 2024-05-01 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('genre', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
    ]
