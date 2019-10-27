from .column import Column
from .table import Table
from .tools import get_table_create_string
import mysql.connector

class DBConnection(object):
	
	def __init__(self, host, user, passwd, database = None):
		self.host = host
		self.user = user
		self.passwd = passwd
		self.database = database
	
	@classmethod
	def __get_db(self):
		conn = mysql.connector.connect(
			host = self.host,
			user = self.user,
			passwd = self.passwd,
			database = self.database)
		cursor = conn.cursor()
		
		return conn, cursor
	
	@classmethod
	def create_table(name: str, *columns: Column):
		conn, cursor = __get_db()
		cursor.execute(get_table_create_string(name, *columns))
		conn.close()
		
		return Table(name, conn= __get_db)
