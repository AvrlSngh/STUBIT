# Generated by Django 2.0.3 on 2018-05-08 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0005_auto_20180508_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='uploaded_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
