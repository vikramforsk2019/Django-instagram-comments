# Generated by Django 3.0.5 on 2020-11-12 09:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(default=0)),
                ('content', models.TextField()),
                ('posted', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('edited', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('thumbsup', models.IntegerField(default='0')),
                ('thumbsdown', models.IntegerField(default='0')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='first_app.Comment')),
            ],
            options={
                'ordering': ['-posted'],
            },
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('image', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'signup',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('file', models.FileField(default='', editable=False, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.BooleanField(default=True)),
                ('comment', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='commentid', to='first_app.Comment')),
                ('user', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='userid', to='first_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('file', models.FileField(default='', editable=False, upload_to='')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('editdate', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='first_app.User')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='thumbs',
            field=models.ManyToManyField(blank=True, default=None, related_name='thumbs', to='first_app.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.User'),
        ),
    ]
