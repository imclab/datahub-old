import sys, logging, time, base64, datetime
from schema.models import *
import schema
from msg_codes import *
from django.utils.timezone import utc
from django.utils.html import escape
from django.core.management import sql, color
from django.db import connection

'''
Datahub Main Controller

@author: Anant Bhardwaj
@date: Mar 21, 2013
'''

def list_databases(username):
	res = {'status':False}
	try:
		user = User.objects.get(username=username)
		databases = Database.objects.filter(owner = user)
		db_names =[database.db_name for database in databases]
		res['status'] = True
		res['db_names'] = db_names			
	except:
		res['code'] = msg_code['UNKNOWN_ERROR']
	logging.debug(res)
	return res



def list_tables(username, db_name):
	res = {'status':False}
	try:
		db = Database.objects.get(db_name=db_name)
		tables = Table.objects.filter(database = db)
		table_names =[table.table_name for table in tables]
		res['status'] = True
		res['table_names'] = table_names			
	except:
		res['code'] = msg_code['UNKNOWN_ERROR']
	logging.debug(res)
	return res
	


def create_database(username, db_name):
	res = {'status':False}
	try:
		user = User.objects.get(username=username)
		db = Database(owner = user, db_name = user.username + '_' + db_name)
		#write_database(user.username + '_' + db_name)
		db.save()
		res['status'] = True				
	except:
		print sys.exc_info()[0]
		res['code'] = msg_code['UNKNOWN_ERROR']
	logging.debug(res)
	return res



def create_table(username, db_name, table_name):
	res = {'status':False}
	try:
		db = Database.objects.get(db_name=username + '_' + db_name)
		table = Table(database = db, table_name = db.db_name + '_' + table_name)
		table.save()
		res['table'] = table
		res['status'] = True				
	except:
		print sys.exc_info()[0]
		res['code'] = msg_code['UNKNOWN_ERROR']
	logging.debug(res)
	return res


def write_database(db_name):
	cursor = connection.cursor()
	cursor.execute('CREATE DATABASE %s' %(db_name))

def write_table(table_name):
	cursor = connection.cursor()
	cursor.execute('CREATE TABLE %s (id int primary key)' %(table_name))
	
