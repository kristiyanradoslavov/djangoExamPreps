# Generated by Django 4.2.2 on 2023-06-17 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0005_alter_album_album_name_alter_album_image_url_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ('pk',)},
        ),
    ]
