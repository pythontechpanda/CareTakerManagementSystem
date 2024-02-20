# Generated by Django 5.0.2 on 2024-02-16 06:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_user_dob_alter_user_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employment',
            name='dependants',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employment',
            name='detail_of',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_info', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employment',
            name='driving_licence_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employment',
            name='leave_allowance',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employment',
            name='line_manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manager', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employment',
            name='marital_status',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employment',
            name='mot_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='employment',
            name='ni_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employment',
            name='passport_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employment',
            name='payroll_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.payrollgroup'),
        ),
        migrations.AlterField(
            model_name='employment',
            name='preferred_travel_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employment',
            name='target_hours',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employment',
            name='visa_expiry_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='employment',
            name='visa_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='equalityanddiversity',
            name='detail_of',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='equalityanddiversity',
            name='disability',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='equalityanddiversity',
            name='ethnicity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ethnicity'),
        ),
        migrations.AlterField(
            model_name='equalityanddiversity',
            name='first_language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.language'),
        ),
        migrations.AlterField(
            model_name='equalityanddiversity',
            name='nationality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.country'),
        ),
        migrations.AlterField(
            model_name='equalityanddiversity',
            name='other_languages',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='equalityanddiversity',
            name='sexual_orientation',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
