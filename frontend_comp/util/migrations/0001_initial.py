# Generated by Django 4.0 on 2022-01-11 20:07

from django.db import migrations, models

import frontend_comp.util.util


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestFileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_field', models.ImageField(upload_to=frontend_comp.util.util.file_url('filez'), verbose_name='foo')),
            ],
            options={
                'verbose_name': 'test',
                'verbose_name_plural': 'tests',
            },
        ),
    ]
