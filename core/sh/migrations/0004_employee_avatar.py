# Generated by Django 5.0.2 on 2024-02-09 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sh', '0003_computer'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='img_avatars/%Y/%m/%d', verbose_name='Avatar'),
        ),
    ]
