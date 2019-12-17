import psycopg2
from postgis import LineString
# from postgis.psycogp import register


db_name = "gis"
db_user = "gis_admin"
db_password = 'New_Password24'
host = "localhost"
port = "5433"
connection = psycopg2.connect("dbname=gis user=gis_admin host=localhost password=New_Password24 port=5432")
print(connection)
cur = connection.cursor()
table = cur.execute('CREATE TABLE IF NOT EXISTS mytable ("geom" geometry(LineString) NOT NULL)')
print(table)