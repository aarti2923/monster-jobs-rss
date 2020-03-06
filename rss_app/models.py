from django.db import models
from first.utils.postgres_connection import Postgresql



class RssCategory():
	def rss_cat_data(self):
		#311, 1274, 1282,1270, 20
		#1251,1274,22,907,311,1282,13,18,1270,5,20,2,786,1000,6,10,17,785,1071,908,19,24,15,1283,1265,1279,1256,1247,1261,1252,1284,1257,1266,1280,1248,1262,1271,1253,1276,1267,1258,1272,1281,1263,1277,1268,1250
		data=Postgresql().get_all("""SELECT * from public.rss_feed_cat where cat_id in (1251,22,907,13,18,5,2);""")
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
			info = requests.get('http://192.168.0.145:8000/api/rss_data/?cat_id=2', headers=headers).json()
			# info = info.split('response')[1]
			for each in info['response']:
				print('pp',each['company'],each['experience'],each['salary'],each['location'],each['qualification'])
				try:
					response = Postgresql().execute_query("""INSERT INTO public.rss_data(company,experience,salary, location,qualification,cat_id) 
					values('{}','{}','{}','{}','{}',2)""".format(each['company'],each['experience'],each['salary'],each['location'],each['qualification']))
				except:
					raise
			# Postgresql().execute_query("""CREATE TABLE IF NOT EXISTS public.rss_data (id bigserial NOT NULL,company varchar(200),experience varchar(200),salary varchar(200),location varchar(200),qualification varchar(200),cat_id integer,loan boolean default false,PRIMARY KEY (id))""")
			print('donee')
		except:
			raise



	def QueryData(self):
		try:
			# Postgresql().execute_query("""DROP TABLE public.rss_data CASCADE;""")
			# Postgresql().execute_query("""CREATE TABLE IF NOT EXISTS public.rss_data (id bigserial NOT NULL,company varchar(200),experience varchar(200),salary varchar(200),location varchar(200),qualification varchar(200),cat_id integer,loan boolean default false,PRIMARY KEY (id))""")
			return 'success'
		except:
			raise