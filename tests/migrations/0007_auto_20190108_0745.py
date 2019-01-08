# Generated by Django 2.1.4 on 2019-01-08 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0006_auto_20190108_0510'),
    ]

    operations = [
        migrations.AddField(
            model_name='studenttestanswer',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questionAnswers', to='tests.TestQuestion'),
        ),
        migrations.AlterField(
            model_name='studenttest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='studenttestanswer',
            name='variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variantAnswers', to='tests.TestQuestionVariant'),
        ),
    ]
