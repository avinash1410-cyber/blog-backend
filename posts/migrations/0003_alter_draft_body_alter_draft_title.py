# Generated by Django 4.0.4 on 2022-06-03 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_post_body_remove_post_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draft',
            name='body',
            field=models.CharField(blank=True, max_length=1000000, null=True),
        ),
        migrations.AlterField(
            model_name='draft',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]