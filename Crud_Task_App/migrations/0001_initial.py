# Generated by Django 5.1.2 on 2024-11-04 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddStudy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studyName', models.CharField(max_length=100)),
                ('studyDescription', models.CharField(max_length=255)),
                ('SutdyPhase', models.CharField(choices=[('phase1', 'phase1'), ('phase2', 'phase2'), ('phase3', 'phase3')], default='phase1', max_length=20)),
                ('SponsorName', models.CharField(max_length=255)),
            ],
        ),
    ]
