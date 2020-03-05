import psycopg2, sys
import psycopg2.extras
from datetime import datetime
class Postgresql(object):
	def __init__(self, dbname='monster', host='localhost', port='5432', username='postgres', password='108'):
		"""
			Create Connection with the database. With credentials passed as parameters. Functions as wrapper for default psycopg2 functions.
		"""
		self.dbname = dbname
		self.host = host
		self.port = port
		self.username = username
		self.password = password

		self.connection, self.cursor = self.start_connection()

	def start_connection(self):
		try:
			connection = psycopg2.connect('dbname={} host={} port={} user={} password={}'.format(self.dbname, self.host, self.port, self.username, self.password))
			cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
			return (connection, cursor)
		except psycopg2.OperationalError:
			print ("Connection Error. Please Check Postgres Credentials or Settings.")
			return None

	def commit_changes(self):
		self.connection.commit()
		self.cursor.close()
		self.connection.close()

	def get_one(self, query):
		self.cursor.execute(query)
		data_dict = self.cursor.fetchone()
		self.commit_changes()
		return data_dict

	def get_all(self, query):
		self.cursor.execute(query)
		data_dicts = self.cursor.fetchall()
		self.commit_changes()
		return data_dicts

	def execute_query(self, query):
		self.cursor.execute(query)
		self.commit_changes()

	def postgres_cursor(self):
		return self.cursor

	def call_procedure(self, procedure_name, *args):
		self.cursor.callproc(procedure_name, tuple(args))
		self.commit_changes()

	def retval_procedure(self, procedure_name, *args):
		self.cursor.callproc(procedure_name, tuple(args))
		data_dicts= self.cursor.fetchall()
		self.commit_changes()
		return data_dicts

	def copy_csv(self, file_object, table_name):
		self.cursor.copy_expert(sql="COPY %s FROM STDIN WITH CSV HEADER DELIMITER AS ','" % table_name, file=file_object)
		self.commit_changes()
	
	def get_csv(self, table_query, name):
		try:
			print (table_query)
			outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(table_query)
			with open(name + '.csv', 'wb') as f:
				self.cursor.copy_expert(outputquery, f)
			self.commit_changes()
			return True
		except:
			raise
			return False

	def execute_query_temp(self, query):
		self.cursor.execute(query)

	def get_all_temp(self, query):
		self.cursor.execute(query)
		data_dicts = self.cursor.fetchall()
		return data_dicts