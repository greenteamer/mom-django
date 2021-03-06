# Generated by Django 2.1.4 on 2019-01-06 10:17

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_auto_20190106_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='studenttestanswer',
            name='answer',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AlterField(
            model_name='studenttestanswer',
            name='variant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='testquestionvariants', to='tests.TestQuestionVariant'),
        ),
    ]
