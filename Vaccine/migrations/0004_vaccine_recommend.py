# Generated by Django 3.1 on 2020-10-16 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vaccine', '0003_delete_vaccine_recommend'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccine_recommend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=1000)),
                ('prevenar_13_total_dose', models.IntegerField()),
                ('prevenar_13_remaining_dose', models.IntegerField()),
                ('prevenar_13_detail_plan', models.CharField(max_length=1000)),
                ('pneumovax_23_remaining_dose', models.IntegerField()),
                ('pneumovax_23_detail_plan', models.CharField(max_length=1000)),
                ('special_conditon', models.CharField(max_length=1000)),
            ],
        ),
    ]
