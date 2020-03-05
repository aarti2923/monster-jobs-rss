from django.db import models
from first.utils.postgres_connection import Postgresql



class RssCategory():
	def rss_cat_data(self):
		data=Postgresql().get_all("""SELECT * from public.rss_feed_cat where cat_id in (1251,1274,22,907,311,1282,13,18,1270,5,20,2,786,1000,6,10,17,785,1071,908,19,24,15,1283,1265,1279,1256,1247,1261,1252,1284,1257,1266,1280,1248,1262,1271,1253,1276,1267,1258,1272,1281,1263,1277,1268,1250);""")
		# print(data)
		return data



class RssData():
	def rss_feed_data(self, cat_id):
		# print(cat_id)
		response = Postgresql().get_all("""SELECT * from public.rss_data where cat_id={} and salary is not null and salary != 'None'""".format(cat_id))
		# print(response)
		return response
