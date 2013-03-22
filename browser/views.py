from django.http import *
from django.shortcuts import render_to_response
from django.utils.encoding import *
import engine.main
from engine.msg_codes import *
from django.core.context_processors import csrf
import json, logging

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

def login(request):
	if request.method == "POST":
		try:
			user = request.POST["user"]
			if(user != ""):
				request.session.flush()
				request.session[SESSION_KEY] = user
				return HttpResponseRedirect(user)
			else:
				return login_form(request)
		except:
			return login_form(request)
	else:
		return login_form(request)
		


def logout(request):
	request.session.flush()
	return HttpResponseRedirect('login')



def index(request, username):
	try:
		return render_to_response("user.html", {'user': username})
	except KeyError:
		return HttpResponseRedirect('login')





	

def list_tables(request, username, database):
	try:
		res = engine.main.list_tables(username, database)
		res.update({'user': username)
		res.update({'database': database)
		return HttpResponse(json.dumps(res), mimetype="application/json")
	except Exception, e:
		logging.debug(e)
		return HttpResponse(request_error, mimetype="application/json")



def list_databases(request, username):
	try:
		res = engine.main.list_databases(username)
		res.update({'user': username)
		return HttpResponse(json.dumps(res), mimetype="application/json")
	except Exception, e:
		logging.debug(e)
		return HttpResponse(request_error, mimetype="application/json")



d