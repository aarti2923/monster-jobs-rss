from django.db import models
from first.utils.postgres_connection import Postgresql



class RssCategory():
	def rss_cat_data(self):
		data=Postgresql().get_all("""SELECT * from public.rss_feed_cat;""")
		# print(data)
		return data



class RssData():
	def rss_feed_data(self, cat_id):
		# print(cat_id)
		response = Postgresql().get_all("""SELECT * from public.rss_data where cat_id={} and salary is not null and salary != 'None'""".format(cat_id))
		# print(response)
		return response


class  CreateTable():
	def RssCreate(self):
		try:
			# Postgresql().execute_query("""CREATE TABLE IF NOT EXISTS public.rss_feed_cat (cat_id integer NOT NULL,cat_name varchar(300) NOT NULL,PRIMARY KEY (cat_id))""")
			# Postgresql().execute_query("""CREATE TABLE IF NOT EXISTS public.rss_data (id bigserial NOT NULL,company varchar(200),experience varchar(200),salary varchar(200),location varchar(200),qualification varchar(200),cat_id integer,loan boolean default false,PRIMARY KEY (id))""")
			import requests
			from ast import literal_eval
			import json
			headers = {'Content-Type':"application/json"}
			info = requests.get('http://192.168.0.145:8000/api/rss_data/?cat_id=907', headers=headers).json()
			# info = info.split('response')[1]
			for each in info['response']:
				print('pp',each['company'],each['experience'],each['salary'],each['location'],each['qualification'])
				try:
					response = Postgresql().execute_query("""INSERT INTO public.rss_data(company,experience,salary, location,qualification,cat_id) 
					values('{}','{}','{}','{}','{}',907)""".format(each['company'],each['experience'],each['salary'],each['location'],each['qualification']))
				except:
					raise
			# Postgresql().execute_query("""CREATE TABLE IF NOT EXISTS public.rss_data (id bigserial NOT NULL,company varchar(200),experience varchar(200),salary varchar(200),location varchar(200),qualification varchar(200),cat_id integer,loan boolean default false,PRIMARY KEY (id))""")
			print('donee')
		except:
			raise



	def QueryData(self):
		data = Postgresql().get_all("""SELECT * from public.rss_data where cat_id=907;""")
		return data