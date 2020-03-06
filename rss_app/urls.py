from django.conf.urls import url
from rss_app import views

urlpatterns = [
				
				url(r'^api/rss_cat/$', views.RssFeedCat, name='rss_cat'),
				url(r'^api/rss_data/$', views.RssFeedData, name='rss_data'),
				url(r'^api/create_table/$', views.RssCreateTable, name='create_table'),
				url(r'^api/query_data/$', views.RssQueryData, name='query_data'),
				
			]