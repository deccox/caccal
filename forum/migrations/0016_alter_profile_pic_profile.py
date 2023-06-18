# Generated by Django 4.2.2 on 2023-06-14 21:52

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0015_alter_profile_pic_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic_profile',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=100, scale=None, size=[200, 200], upload_to='profile-img/'),
        ),
    ]