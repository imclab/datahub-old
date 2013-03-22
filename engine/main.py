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
	


def create_database(username, database):
	res = {'status':False}
	logging.debug(res)
	return res



def create_table(username, database, table):
	res = {'status':False}
	logging.debug(res)
	return res
