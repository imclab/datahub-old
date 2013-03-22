from django.db import models

'''
Datahub Models

@author: Anant Bhardwaj
@date: Mar 21, 2013
'''



class User(models.Model):
	id = models.AutoField(primary_key=True)
	email = models.CharField(max_length=50, unique = True)
	username = models.CharField(max_length=50, unique = True)
	password = models.CharField(max_length=50)
	active = models.BooleanField(default=True)
	def __unicode__(self):
		return self.name

	class Meta:
		db_table = "datahub_users"


class Database(models.Model):
	id = models.AutoField(primary_key=True)
	db_name = models.CharField(max_length=20, unique = True)
	owner = models.ForeignKey('User')
	timestamp = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.name

	class Meta:
		db_table = "datahub_databases"


class Table(models.Model):
	id = models.AutoField(primary_key=True)
	table_name = models.CharField(max_length=20, unique = True)
	database = models.ForeignKey('Database')
	timestamp = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.name

	class Meta:
		db_table = "datahub_tables"




