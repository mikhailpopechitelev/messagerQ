# Generated by Django 4.2.7 on 2023-11-17 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0008_chatparticipant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=100)),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chats.user')),
            ],
        ),
    ]
