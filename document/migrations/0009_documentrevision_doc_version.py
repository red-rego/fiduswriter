# Generated by Django 2.2.2 on 2019-06-23 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0008_documenttemplate_doc_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentrevision',
            name='doc_version',
            field=models.DecimalField(decimal_places=1, default=3.0, max_digits=3),
        ),
    ]
