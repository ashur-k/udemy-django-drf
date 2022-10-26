# Generated by Django 3.2.11 on 2022-10-22 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('value', models.IntegerField(choices=[(1, 'poor'), (2, 'fair'), (3, 'good'), (4, 'very good'), (5, 'excellent')], default=0, help_text='1=Poor, 2=Fair, 3=Good, 4=Very Good, 5=Excellent', verbose_name='rating value')),
                ('review', models.TextField(blank=True, verbose_name='rating review')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_ratings', to='articles.article')),
                ('rated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_who_rated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('rated_by', 'article')},
            },
        ),
    ]
