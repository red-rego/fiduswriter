# Generated by Django 1.11.13 on 2018-08-14 17:09
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import document.models


class Migration(migrations.Migration):

    replaces = [('document', '0001_initial'), ('document', '0002_auto_20151230_1732'), ('document', '0003_auto_20160104_0329'), ('document', '0004_auto_20160104_0512'), ('document', '0005_auto_20160119_0716'), ('document', '0006_auto_20160130_0708'), ('document', '0007_auto_20160130_0709'), ('document', '0008_auto_20160515_0838'), ('document', '0009_auto_20160515_0847'), ('document', '0010_auto_20160515_0849'), ('document', '0011_auto_20160515_0925'), ('document', '0012_exporttemplate'), ('document', '0013_auto_20161003_1756'), ('document', '0014_auto_20161008_0305'), ('document', '0015_auto_20161018_0531'), ('document', '0016_auto_20161031_1616'), ('document', '0017_submission'), ('document', '0018_submission_user'), ('document', '0019_auto_20161212_0657'), ('document', '0020_submittedaccessright_submission_id'), ('document', '0021_auto_20161212_0746'), ('document', '0017_auto_20161217_0320'), ('document', '0022_merge_20161219_0605'), ('document', '0023_auto_20170122_0525'), ('document', '0024_auto_20170604_1811'), ('document', '0025_auto_20170612_1123'), ('document', '0026_auto_20170810_0956'), ('document', '0027_auto_20170810_0957'), ('document', '0028_remove_document_settings'), ('document', '0029_auto_20170810_1130'), ('document', '0030_document_bibliography'), ('document', '0031_auto_20180324_1935'), ('document', '0032_document_listed')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessRight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rights', models.CharField(choices=[('r', 'read'), ('w', 'read/write')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=255)),
                ('contents', models.TextField(default='{}')),
                ('metadata', models.TextField(default='{}')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentRevision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(blank=True, default='', max_length=255)),
                ('date', models.DateTimeField(auto_now=True)),
                ('file_object', models.FileField(upload_to=document.models.revision_filename)),
                ('file_name', models.CharField(blank=True, default='', max_length=255)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.Document')),
            ],
        ),
        migrations.AddField(
            model_name='accessright',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.Document'),
        ),
        migrations.AddField(
            model_name='accessright',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='accessright',
            name='rights',
            field=models.CharField(choices=[('r', 'reader'), ('w', 'author'), ('e', 'editor'), ('c', 'reviewer')], max_length=3),
        ),
        migrations.AlterField(
            model_name='accessright',
            name='rights',
            field=models.CharField(choices=[('r', 'reader'), ('w', 'author'), ('e', 'editor'), ('c', 'reviewer')], max_length=1),
        ),
        migrations.AlterField(
            model_name='accessright',
            name='rights',
            field=models.CharField(choices=[('r', 'reader'), ('w', 'author'), ('e', 'editor'), ('c', 'reviewer'), ('o', 'comment_only')], max_length=1),
        ),
        migrations.AlterField(
            model_name='accessright',
            name='rights',
            field=models.CharField(choices=[('r', 'reader'), ('w', 'author'), ('e', 'editor'), ('c', 'reviewer'), ('o', 'comment_only')], max_length=7),
        ),
        migrations.AlterField(
            model_name='accessright',
            name='rights',
            field=models.CharField(choices=[('read', 'Reader'), ('write', 'Writer'), ('edit', 'Editor'), ('review', 'Reviewer'), ('comment', 'Commentator')], max_length=7),
        ),
        migrations.AlterField(
            model_name='accessright',
            name='rights',
            field=models.CharField(choices=[('read', 'Reader'), ('read-without-comments', 'Read without comments'), ('write', 'Writer'), ('review', 'Reviewer'), ('comment', 'Commentator'), ('edit', 'Editor')], max_length=21),
        ),
        migrations.AlterField(
            model_name='accessright',
            name='rights',
            field=models.CharField(choices=[('read', 'Reader'), ('read-without-comments', 'Reader without comment access'), ('write', 'Writer'), ('review', 'Reviewer'), ('comment', 'Commentator'), ('edit', 'Editor')], max_length=21),
        ),
        migrations.AlterField(
            model_name='accessright',
            name='rights',
            field=models.CharField(choices=[('read', 'Reader'), ('read-without-comments', 'Reader without comment access'), ('write', 'Writer'), ('write-tracked', 'Write with tracked changes'), ('review', 'Reviewer'), ('comment', 'Commentator'), ('edit', 'Editor')], max_length=21),
        ),
        migrations.AlterUniqueTogether(
            name='accessright',
            unique_together=set([('document', 'user')]),
        ),
        migrations.AddField(
            model_name='document',
            name='diff_version',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='document',
            name='last_diffs',
            field=models.TextField(default='[]'),
        ),
        migrations.AddField(
            model_name='document',
            name='version',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='document',
            name='comment_version',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='document',
            name='comments',
            field=models.TextField(default='{}'),
        ),
        migrations.CreateModel(
            name='ExportTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(blank=True, default='', max_length=255)),
                ('file_type', models.CharField(choices=[('docx', 'Docx'), ('odt', 'ODT')], max_length=5)),
                ('template_file', models.FileField(upload_to=document.models.template_filename)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='exporttemplate',
            unique_together=set([('file_name', 'file_type')]),
        ),
        migrations.RemoveField(
            model_name='document',
            name='comment_version',
        ),
        migrations.RemoveField(
            model_name='document',
            name='diff_version',
        ),
        migrations.RemoveField(
            model_name='document',
            name='metadata',
        ),
        migrations.AddField(
            model_name='document',
            name='doc_version',
            field=models.DecimalField(decimal_places=1, default=2.0, max_digits=3),
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='document',
            name='bibliography',
            field=models.TextField(default='{}'),
        ),
        migrations.AlterField(
            model_name='document',
            name='doc_version',
            field=models.DecimalField(decimal_places=1, default=2.1, max_digits=3),
        ),
        migrations.AddField(
            model_name='document',
            name='listed',
            field=models.BooleanField(default=True),
        ),
    ]
