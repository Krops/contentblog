# Generated by Django 2.0.3 on 2018-03-14 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpage', '0002_auto_20180314_2123'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=False, to='blogpage.Post'),
        ),
    ]
