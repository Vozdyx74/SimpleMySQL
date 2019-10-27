from .column import Column
from .errors import MissingUserError
from .table import Table
from .tools import get_table_create_string
import mysql.connector

class DBConnection(object):
	
	def __init__(self, host: str= 'localhost', user: str= None, passwd: str= ' ', database: str= None):
		if not user:
			raise MissingUserError
		self.host = host
		self.user = user
		self.passwd = passwd
		self.database = database
		c, cu = self.__get_connection()
		c.close()
	
	@classmethod
	def __get_connection(self):
		conn = mysql.connector.connect(
			host = self.host,
			user = self.user,
			passwd = self.passwd,
			database = self.database)
		cursor = conn.cursor()
		
		return conn, cursor
	
	@classmethod
	def create_table(self, name: str, *columns: Column):
		conn, cursor = __get_connection()
		try:
			cursor.execute(get_table_create_string(name, *columns))
			conn.close()
		except Exception as e:
			conn.close()
			raise e
		
		return Table(name, db= self)

	@classmethod
	def get_table(self, name: str):
		return Table(name, db= self)