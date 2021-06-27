# Generated by Django 3.2.4 on 2021-06-21 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rest_api', 'create_superuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField()),
                ('data_year', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('semester', models.CharField(choices=[('FIRST', 'A'), ('SECOND', 'B'), ('SUMMER', 'Summer'), ('EITHER', 'Either'), ('ANNUAL', 'Annual')], max_length=6)),
                ('is_given_this_year', models.BooleanField()),
                ('points', models.FloatField()),
                ('is_corner_stone', models.BooleanField(null=True)),
                ('comment', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CourseGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_type', models.CharField(choices=[('MUST', 'Must'), ('CHOICE', 'Choice'), ('CHOOSE_FROM_LIST', 'From List'), ('CORNER_STONE', 'Corner Stone'), ('SUPPLEMENTARY', 'Supplementary')], max_length=20)),
                ('year_in_studies', models.IntegerField()),
                ('index_in_track_year', models.IntegerField()),
                ('required_course_count', models.IntegerField(null=True)),
                ('required_points', models.IntegerField(null=True)),
                ('comment', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hug',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_in_studies', models.IntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth'), (5, 'Fifth'), (6, 'Sixth'), (7, 'Seventh')])),
            ],
        ),
        migrations.CreateModel(
            name='Take',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_in_studies', models.IntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth'), (5, 'Fifth'), (6, 'Sixth'), (7, 'Seventh')])),
                ('semester', models.CharField(choices=[('FIRST', 'A'), ('SECOND', 'B'), ('SUMMER', 'Summer'), ('EITHER', 'Either'), ('ANNUAL', 'Annual')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('track_number', models.IntegerField()),
                ('data_year', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('points_must', models.IntegerField()),
                ('points_from_list', models.IntegerField()),
                ('points_choice', models.IntegerField()),
                ('points_complementary', models.IntegerField()),
                ('points_corner_stones', models.IntegerField()),
                ('points_minor', models.IntegerField()),
                ('points_additional_hug', models.IntegerField()),
                ('comment', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.AddConstraint(
            model_name='track',
            constraint=models.UniqueConstraint(fields=('track_number', 'data_year'), name='track_year'),
        ),
        migrations.AddField(
            model_name='take',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.course'),
        ),
        migrations.AddField(
            model_name='take',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.student'),
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, through='rest_api.Take', to='rest_api.Course'),
        ),
        migrations.AddField(
            model_name='student',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.track'),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hug',
            name='courses',
            field=models.ManyToManyField(to='rest_api.Course'),
        ),
        migrations.AddField(
            model_name='coursegroup',
            name='courses',
            field=models.ManyToManyField(to='rest_api.Course'),
        ),
        migrations.AddField(
            model_name='coursegroup',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.track'),
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('course_id', 'data_year')},
        ),
        migrations.AddConstraint(
            model_name='coursegroup',
            constraint=models.UniqueConstraint(fields=('track', 'year_in_studies', 'course_type', 'index_in_track_year'), name='group_unique'),
        ),
    ]
