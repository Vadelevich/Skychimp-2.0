# Generated by Django 4.1.5 on 2023-01-25 08:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('service', '0004_alter_mailing_first_date_alter_mailing_last_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='TryMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='дата и время последней попытки')),
                ('status', models.CharField(max_length=15, verbose_name='статус попытки')),
                ('answer',
                 models.CharField(blank=True, max_length=150, null=True, verbose_name='ответ почтового сервера')),
            ],
        ),
    ]