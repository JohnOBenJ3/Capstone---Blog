# Generated by Django 3.0 on 2019-12-09 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191209_1759'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['-created_on']},
        ),
    ]
