import urllib.request
import json
import re
import xmltodict
import pprint
from html2text import html2text
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from first.utils.postgres_connection import Postgresql


wp = urllib.request.urlopen("https://www.monsterindia.com/jobsearch/rss_jobs.html?cat=1250")
# print()

pw = wp.read()

pp = pprint.PrettyPrinter(indent=4) 
x= json.dumps(xmltodict.parse(pw)) 
response = (json.loads(x)) 
# print(response)
count=1 
for each in response['rss']['channel']['item']: 
	txt = html2text(each['description']) 
	lines = str(txt).replace("**","").replace("-fication -", ":").strip().splitlines() 
	fields = [[field.strip() for field in line.split(":")] for line in lines if ':' in line]	 
	try: 
		info = dict(fields) 
		# print(info)
		response = Postgresql().execute_query("""INSERT INTO public.rss_data(company,experience,salary, location,qualification,cat_id) 
		values('{}','{}','{}','{}','{}',1250)""".format(info.get('Company'),info.get('Experience'),info.get('Salary'),info.get('location'),info.get('Qualification')))
		# print('responses',info) 
		# print(info.get('Salary'))  
		# print(info.get('Company')) 
		# print(info.get('Qualification')) 
		# print(info.get('Experience')) 
		# print(info.get('location')) 
		# count+=1

	except Exception as e:
		print(count,e)
		pass

		# raise




#Comany
# Qualification
# Expr
# Salary
# Location



#Done Cat
##1274    #1277
##907     #1268
##3       #1250
#11      #1282
##22
#13
#14
#18
#1270
#5
#20
#2
#786
#1000
#6
#10
#17
#785
#1071
#908
#23
#19
#24
## 1251
#15
#1283
##1274
#1265
#1279
#1256
#1279
#1247
#1261
#1252
#1284
#1257
#1266
#1280
#1248
#1262
#1271
#1253
#1276
#1267
#1258
#1272
#1281
#1263
#1254




#7
#9
#16
#1249
#1259
#23
#14
#15


















# 1251
#1274
#22
#907
#3