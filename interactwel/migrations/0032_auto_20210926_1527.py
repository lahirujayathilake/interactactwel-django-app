# Generated by Django 2.2.23 on 2021-09-26 15:27

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('interactwel', '0031_auto_20210108_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='subbasin',
            name='basline_json',
            field=jsonfield.fields.JSONField(default='{}'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subbasin',
            name='project_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='interactwel.InteractwelProject'),
        ),
        migrations.AddField(
            model_name='subbasin',
            name='subbasin_type',
            field=models.CharField(default='', max_length=64),
        ),
    ]