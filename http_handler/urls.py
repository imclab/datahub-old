from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
     url(r'^logout', 'browser.views.logout'),
     url(r'^login', 'browser.views.login'),
     url(r'^$', 'browser.views.user'),
	 url(r'^(\w+)$', 'browser.views.user'),
	 url(r'^(\w+)/(\w+)$', 'browser.views.database'),
	 url(r'^(\w+)/(\w+)/(\w+)$', 'browser.views.table'),
	
	 
	
)
