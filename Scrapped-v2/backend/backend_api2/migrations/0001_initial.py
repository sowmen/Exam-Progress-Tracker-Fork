# Generated by Django 3.2 on 2021-06-23 01:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('year', models.CharField(default=2021, max_length=4)),
                ('semester', models.CharField(choices=[('1/1', '1/1'), ('1/2', '1/2'), ('2/1', '2/1'), ('2/2', '2/2'), ('3/1', '3/1'), ('3/2', '3/2'), ('4/1', '4/1'), ('4/2', '4/2')], default='1/1', max_length=10)),
                ('committee_id', models.CharField(editable=False, max_length=250, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('course_title', models.CharField(max_length=100)),
                ('course_credit', models.FloatField()),
                ('course_type', models.CharField(choices=[('theory', 'Theory'), ('lab', 'Lab')], default='Theory', max_length=10)),
                ('session', models.CharField(max_length=250)),
                ('committee_code', models.ForeignKey(default='unassigned', on_delete=django.db.models.deletion.SET_DEFAULT, to='backend_api2.committee')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('initials', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('is_dept_head', models.BooleanField(default=False)),
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Deadline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('details', models.TextField()),
                ('status', models.CharField(choices=[('complete', 'Completed'), ('incomplete', 'Incomplete')], default='Incomplete', max_length=20)),
                ('committee_deadline', models.ForeignKey(blank=True, default='unassigned', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='backend_api2.committee')),
                ('course_code', models.ForeignKey(blank=True, default='unassigned', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='backend_api2.course')),
                ('teacher', models.ForeignKey(default='unassigned', on_delete=django.db.models.deletion.SET_DEFAULT, to='backend_api2.teacher')),
            ],
            options={
                'ordering': ('date',),
            },
        ),
        migrations.AddField(
            model_name='course',
            name='teacher_code',
            field=models.ForeignKey(default='unassigned', on_delete=django.db.models.deletion.SET_DEFAULT, to='backend_api2.teacher'),
        ),
        migrations.AddField(
            model_name='committee',
            name='teachers',
            field=models.ManyToManyField(to='backend_api2.Teacher'),
        ),
    ]
