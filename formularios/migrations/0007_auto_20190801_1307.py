# Generated by Django 2.0.13 on 2019-08-01 18:07

from django.db import migrations, models
import formularios.models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0006_auto_20190711_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to=formularios.models.get_image_path),
        ),
    ]