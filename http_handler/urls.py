from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
     url(r'^logout', 'browser.views.logout'),
     url(r'^login', 'browser.views.login'),
     url(r'^register', 'browser.views.register'),
     url(r'^new_database/(\w+)/(\w+)$', 'browser.views.new_database'),
     url(r'^new_table/(\w+)/(\w+)$', 'browser.views.new_table'),
     url(r'^$', 'browser.views.user'),
	 url(r'^(\w+)$', 'browser.views.user'),
	 url(r'^(\w+)/(\w+)$', 'browser.views.database'),
	 url(r'^(\w+)/(\w+)/(\w+)$', 'browser.views.table'),
	
	 
	
)
