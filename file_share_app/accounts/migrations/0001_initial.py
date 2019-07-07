# Generated by Django 2.2.2 on 2019-07-07 11:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Filedb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='books/pdfs/')),
                ('description', models.CharField(choices=[('video', 'VIDIO'), ('audio', 'AUDIO'), ('file', 'FILE'), ('pdf', 'PDF')], default='file', max_length=6)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='books/covers/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
