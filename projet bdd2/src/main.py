import lib.Fonction as X
import lib.creat_base as B

#X.removed(X.adresse() +'//..//..//data//ma_base.db')

Base = B.BDD()

x = """CREATE TABLE STATION 
(ID INTEGER PRIMARY KEY, 
CITY CHAR(20), 
STATE CHAR(2), 
LAT_N REAL, 
LONG_W REAL); """
Base.request(x)



x = """INSERT INTO STATION VALUES (13, 'Phoenix', 'AZ', 33, 112);""" 
Base.request(x)
x = """INSERT INTO STATION VALUES (44, 'Denver', 'CO', 40, 105);"""
Base.request(x)
x = """INSERT INTO STATION VALUES (66, 'Caribou', 'ME', 47, 68);"""
Base.request(x)

x = "SELECT * FROM STATION"
text = Base.request(x)

print(text)
