# Generated by Django 3.0 on 2019-12-18 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('recipies', '0002_auto_20191210_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.Category'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image_url',
            field=models.CharField(max_length=255),
        ),
    ]