# Generated by Django 4.0.8 on 2023-10-21 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_rename_create_at_project_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='projects/images/'),
        ),
    ]
