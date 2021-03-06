# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 23:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('titre', models.CharField(db_column='Titre', max_length=25)),
                ('description', models.TextField(db_column='Description')),
                ('urlimage', models.CharField(db_column='URlImage', max_length=255)),
                ('dateajout', models.DateTimeField(db_column='DateAjout')),
                ('datederniermodif', models.DateTimeField(blank=True, db_column='DateDernierModif', null=True)),
            ],
            options={
                'db_table': 'categorie',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Couleur',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('titre', models.CharField(db_column='Titre', max_length=25)),
                ('urlimage', models.CharField(db_column='URlImage', max_length=150)),
                ('dateajout', models.DateTimeField(db_column='DateAjout')),
                ('datederniermodif', models.DateTimeField(blank=True, db_column='DateDernierModif', null=True)),
            ],
            options={
                'db_table': 'couleur',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('reference', models.CharField(db_column='Reference', max_length=55)),
                ('designation', models.CharField(db_column='Designation', max_length=150)),
                ('description', models.TextField(db_column='Description')),
                ('disponibilite', models.CharField(db_column='Disponibilite', max_length=3)),
                ('prix', models.FloatField(blank=True, db_column='Prix', null=True)),
                ('nouveau', models.CharField(db_column='Nouveau', max_length=3)),
                ('garantie', models.CharField(blank=True, db_column='Garantie', max_length=3, null=True)),
                ('dureegarantie', models.IntegerField(blank=True, db_column='DureeGarantie', null=True)),
                ('urlimage', models.CharField(db_column='UrlImage', max_length=255)),
                ('dateajout', models.DateTimeField(db_column='DateAjout')),
                ('datedernmodif', models.DateTimeField(blank=True, db_column='DateDernModif', null=True)),
            ],
            options={
                'db_table': 'produit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Realisation',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('reference', models.CharField(db_column='Reference', max_length=10)),
                ('titre', models.CharField(db_column='Titre', max_length=25)),
                ('urlimage', models.CharField(db_column='URlImage', max_length=255)),
                ('daterealisation', models.DateField(blank=True, db_column='DateRealisation', null=True)),
                ('dateajout', models.DateTimeField(db_column='DateAjout')),
                ('datederniermodif', models.DateTimeField(blank=True, db_column='DateDernierModif', null=True)),
            ],
            options={
                'db_table': 'realisation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('titre', models.CharField(db_column='Titre', max_length=25)),
                ('description', models.TextField(db_column='Description')),
                ('logoservice', models.CharField(db_column='LogoService', max_length=150)),
                ('dateajout', models.DateTimeField(db_column='DateAjout')),
                ('datederniermodif', models.DateTimeField(blank=True, db_column='DateDernierModif', null=True)),
            ],
            options={
                'db_table': 'service',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Souscategorie',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('titre', models.CharField(db_column='Titre', max_length=100)),
                ('description', models.TextField(db_column='Description')),
                ('dateajout', models.DateTimeField(db_column='DateAjout')),
                ('datedernmodif', models.DateTimeField(blank=True, db_column='DateDernModif', null=True)),
            ],
            options={
                'db_table': 'souscategorie',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('nom', models.CharField(db_column='Nom', max_length=150)),
                ('prenom', models.CharField(db_column='Prenom', max_length=150)),
                ('role', models.CharField(max_length=20)),
                ('login', models.CharField(db_column='Login', max_length=255)),
                ('password', models.CharField(db_column='Password', max_length=255)),
                ('etatcompte', models.CharField(db_column='EtatCompte', max_length=15)),
                ('dateajout', models.DateTimeField(db_column='DateAjout')),
                ('datedernconx', models.DateTimeField(blank=True, db_column='DateDernconx', null=True)),
                ('datedernmodif', models.DateTimeField(blank=True, db_column='DateDernModif', null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Couleurproduit',
            fields=[
                ('produitid', models.ForeignKey(db_column='ProduitId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Distrat_ma.Produit')),
                ('couleurid', models.ForeignKey(db_column='CouleurId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, to='Distrat_ma.Couleur')),
                ('urlimage', models.CharField(blank=True, db_column='URlImage', max_length=200, null=True)),
                ('dateajout', models.DateTimeField(db_column='DateAjout')),
            ],
            options={
                'db_table': 'couleurproduit',
                'managed': False,
            },
        ),
    ]
