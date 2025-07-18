# Generated by Django 5.2.4 on 2025-07-16 02:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_dash', '0003_testreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='testreport',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='testreport',
            name='status',
            field=models.TextField(default='in_progress', max_length=255),
        ),
        migrations.AlterField(
            model_name='testreport',
            name='test_id',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.CreateModel(
            name='TestReportImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='test_reports/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('test_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='user_dash.testreport')),
            ],
        ),
    ]
