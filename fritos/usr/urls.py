from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:

    url(r'^login/$', views.login, name="login"),
	url(r'^login/do/$', views.login_do, name="login_do"),
	url(r'^logout/$', views.logout, name="logout"),
)
