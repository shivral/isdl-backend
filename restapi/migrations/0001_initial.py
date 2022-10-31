# Generated by Django 4.1.2 on 2022-10-31 20:41

from django.conf import settings
import django.contrib.auth.models
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40, unique=True)),
                ('isAdmin', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('hall_name', models.CharField(max_length=40)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hall_location', models.CharField(max_length=40)),
                ('hall_capacity', models.IntegerField()),
                ('hall_rating', models.IntegerField()),
                ('hall_image', models.URLField()),
                ('hall_selectedslots', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='LectureHall',
            fields=[
                ('hall_name', models.CharField(max_length=40)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hall_location', models.CharField(max_length=40)),
                ('hall_capacity', models.IntegerField()),
                ('hall_rating', models.IntegerField()),
                ('hall_image', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked', models.BooleanField()),
                ('pending', models.BooleanField()),
                ('slotStart', models.DateTimeField(blank=True, null=True)),
                ('slotEnd', models.DateTimeField(blank=True, null=True)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.lecturehall')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='bookings',
            field=models.ManyToManyField(through='restapi.Booking', to='restapi.lecturehall'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
