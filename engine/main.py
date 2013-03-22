import sys, logging, time, base64, datetime
from schema.models import *
from msg_codes import *
from django.utils.timezone import utc
from django.utils.html import escape

'''
Datahub Main Controller

@author: Anant Bhardwaj
@date: Mar 21, 2013
'''

def list_databases(username):
	res = {'status':False}
	logging.debug(res)
	return res



def list_tables(username, database):
	res = {'status':False}
	logging.debug(res)
	return res
	


def create_database(username, db_name):
	res = {'status':False}
	try:
		user = User.objects.get(username=username)
		db =Database(user, username + '_' + db_name)
		db.save()
		res=['status'] = True				
	except:
		res['code'] = msg_code['UNKNOWN ERROR']
	logging.debug(res)
	return res



def create_table(username, db_name, table_name):
	res = {'status':False}
	try:
		user = User.objects.get(username=username)
		db = Database.objects.get(db_name=user.username + '_' + db_name)
		table = Table(user, db, user.username + '_' + db.db_name + '_' + table_name)
		table.save()
		res=['status'] = True				
	except:
		res['code'] = msg_code['UNKNOWN ERROR']
	logging.debug(res)
	return res
