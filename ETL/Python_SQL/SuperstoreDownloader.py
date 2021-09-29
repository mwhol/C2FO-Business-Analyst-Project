import pandas as pd
import requests
import sqlite3
import os

def main():
	# Create your connection.
	cnx = sqlite3.connect('Superstore.sql')

	url = "https://community.tableau.com/sfc/servlet.shepherd/document/download/0694T000001GnpUQAS?operationContext=S1"
	filename = "Superstore.xls"

	r = requests.get(url)
	f = open(filename, 'wb')
	for chunk in r.iter_content(chunk_size=512 * 1024): 
	    if chunk:
	        f.write(chunk)
	f.close()

	xls = pd.ExcelFile(filename)

	orders = pd.read_excel(xls, 'Orders')
	returns = pd.read_excel(xls, 'Returns')
	people = pd.read_excel(xls, 'People')

	orders.to_sql('Orders', con=cnx)
	returns.to_sql('Returns', con=cnx)
	people.to_sql('People', con=cnx)

	cnx.cursor().execute('''SELECT 1 FROM orders''')
	cnx.close()

	os.rename("Superstore.sql", "Superstore.db")
	
	with open("Cleanup.sql", "r") as sql_file:
		sql_script = sql_file.read()

	db = sqlite3.connect("Superstore.db")
	cursor = db.cursor()
	cursor.executescript(sql_script)
	db.commit()
	db.close()


if __name__ == "__main__":
    main()