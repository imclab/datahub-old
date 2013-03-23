from django.http import *
from django.shortcuts import render_to_response
from django.utils.encoding import *
import engine.main
from engine.msg_codes import *
from django.core.context_processors import csrf
import json, logging
from schema.models import *

'''
@author: Anant Bhardwaj
@date: Mar 21, 2013

Datahub Web Handler
'''

request_error = json.dumps({'code': msg_code['REQUEST_ERROR'],'status':False})
SESSION_KEY = 'USER'

def init_session(email):
	pass

def login_form(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)


def register_form(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('register.html', c)

def login(request):
	if request.method == "POST":
		try:
			username = request.POST["username"]
			password = request.POST["password"]
			if(username != "" and password!= ""):
				user = User.objects.get(username=username, password=password)
				request.session.flush()
				request.session[SESSION_KEY] = user.username
				return HttpResponseRedirect("/" + user.username)
			else:
				return login_form(request)
		except:
			return login_form(request)
	else:
		return login_form(request)
		
def register(request):
	if request.method == "POST":
		username = request.POST["username"]
		email = request.POST["email"]
		password = request.POST["password"]
		if(username != "" and password != "" and email!=""):
			user = User(username=username, email=email, password=password)
			user.save()
			request.session.flush()
			request.session[SESSION_KEY] = user.username
			return HttpResponseRedirect("/" + user.username)
		else:
			return register_form(request)
	else:
		return register_form(request)




def logout(request):
	request.session.flush()
	return HttpResponseRedirect('/login')



def user(request, username=None):
	try:
		if(username):
			res = engine.main.list_databases(username)
			return render_to_response("user.html", {'username': username, 'db_names':res['db_names']})
		else:
			user = request.session[SESSION_KEY]
			return HttpResponseRedirect(user)
	except KeyError:
		return HttpResponseRedirect('/login')






def new_database(request, username, db_name):
	engine.main.create_database(username, db_name)
	return HttpResponseRedirect("/"+username)


def new_table(request, username, db_name):
	return render_to_response("new_table.html", {'username': username, 'db_name':db_name})



def database(request, username, db_name):
	try:
		res = engine.main.list_tables(db_name)
		return render_to_response("database.html", {'username': username, 'db_name':db_name, 'table_names':res['table_names']})
	except Exception, e:
		logging.debug(e)
		return HttpResponse(request_error, mimetype="application/json")


	

def table(request, username, db_name, table_name):
	try:
		return render_to_response("table.html", {'username': username, 'db_name':db_name, 'table_name':table_name})
	except Exception, e:
		logging.debug(e)
		return HttpResponse(request_error, mimetype="application/json")



