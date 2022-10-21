#!/usr/bin/python

""" ElementData To Sqlite """

import sqlite3

__author__ = "Badri Gs"
__email__ = "badri.gs999@gmail.com"


class ElementToSqlite:

	def __init__(self, element_data, sqlite_filepath):
		
		# Create Sqlite Connection & Cursor
		self.connection = sqlite3.connect(sqlite_filepath)
		self.cursor = self.connection.cursor()

		# Initiatizer
		self.createTable()
		self.recursiveInsert(root)

	def __str__(self):
		self.cursor.execute('SELECT * FROM element;')
		result = self.cursor.fetchall()
		return "\n".join(map(str, result))

	def createTable(self):
		"""Drop & Create Table for element"""

		self.cursor.execute("""
			CREATE TABLE element (
				id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
				element_name TEXT NOT NULL,
				element_type TEXT NOT NULL,
				 INTEGER REFERENCES element(id),
				full_path TEXT
			);
		""")
		self.connection.commit()


	def searchDB(self, object_full_path):
		"""Search and Get the Parent ID for the given object_fullpath""" 

		self.cursor.execute("SELECT id FROM element WHERE full_path=?", (object_full_path, ))
		result = self.cursor.fetchone()
		return result[0] if result else 'NULL'

	def insertIntoDB(self, parent_fullname, element):
		self.cursor.execute('INSERT INTO element (object_name, object_type, parent_id, full_path) VALUES (?, ?, ?, ?)', (
			element.get('name'), element.tag, self.searchDB(parent_fullname), element.get("fullPath")
		))
		self.connection.commit()

	def recursiveInsert(self, root):
		"""Generate XML Data -> DB Structure"""
		for child in list(root):
			self.insertIntoDB(root.get("fullPath"), child)
			self.recursiveInsert(child)
