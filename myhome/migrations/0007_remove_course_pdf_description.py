# Generated by Django 3.2.3 on 2021-07-18 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0006_remove_course_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_pdf',
            name='description',
        ),
    ]