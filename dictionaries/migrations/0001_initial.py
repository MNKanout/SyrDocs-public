# Generated by Django 3.0.4 on 2020-06-18 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_name', models.CharField(max_length=50)),
                ('word_translation', models.CharField(max_length=50)),
                ('word_note', models.CharField(max_length=100)),
                ('blog_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.BlogPost')),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'dictionaries',
            },
        ),
    ]