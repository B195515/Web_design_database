#!/localdisk/anaconda3/bin/python
import sys
# get sys package for file arguments etc
import pymysql

# Connect to database
con = pymysql.connect(host='localhost', user='s2255686', passwd='qeenreen', db='s2255686')
cur = con.cursor()

# Print usage message if no arguments detected
if len(sys.argv) != 2:
  print("Usage: addsmiles.py manufacturer")
  sys.exit(-1)

# Get manufacturer name as argument
manuname = sys.argv[1]
input_name = manuname+".smi"

# Select data by manufacturer
sql = "SELECT id FROM Manufacturers WHERE name='%s'" % (manuname)
cur.execute(sql)
row = cur.fetchone()
supid = row[0]
with open(input_name,"r") as fi:
  for line in fi:
    elems = line.split()
    name = elems[0]
    sml = elems[1]
    sql = "Select id from Compounds where catn='%s' and ManuID='%s'" % (name,supid)
    cur.execute(sql)
    row = cur.fetchone()
    cid = row[0]
    sql = "insert into Smiles (cid,smiles) values (%s,'%s')" % (cid,sml)
    #print(sql,"\n")
    cur.execute(sql)
con.commit()
con.close()
