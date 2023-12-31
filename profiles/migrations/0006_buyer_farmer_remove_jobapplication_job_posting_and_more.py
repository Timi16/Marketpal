# Generated by Django 4.0 on 2023-08-14 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_first_name_alter_user_last_name'),
        ('profiles', '0005_remove_worker_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='authentication.user')),
            ],
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='farmer', to='authentication.user')),
            ],
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='job_posting',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='worker',
        ),
        migrations.RemoveField(
            model_name='jobposting',
            name='employer',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='user',
        ),
        migrations.DeleteModel(
            name='Employer',
        ),
        migrations.DeleteModel(
            name='JobApplication',
        ),
        migrations.DeleteModel(
            name='JobPosting',
        ),
        migrations.DeleteModel(
            name='Worker',
        ),
    ]
