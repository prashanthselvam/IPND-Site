from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^notes/$', views.notes, name='notes'),
	url(r'^age_in_days/$', views.age_in_days, name='age_in_days'),
	url(r'^guestbook/$', views.guestbook, name='guestbook'),
]