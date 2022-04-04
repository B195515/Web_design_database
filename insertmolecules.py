#!/localdisk/anaconda3/bin/python3
import sys
# get sys package for file arguments etc
import pymysql
import base64

con = pymysql.connect(host='localhost', user='s2255686', passwd='qeenreen', db='s2255686')
cur = con.cursor()

if(len(sys.argv) != 2) :
  print("Usage: testmol.py dbname")
  sys.exit(-1)

# Takes the sdf file as input file
manuname = sys.argv[1]
input_name = manuname+".sdf"

# Get man id from the Manufacturers table, filtered by the manufacturer name
sql = "SELECT id FROM Manufacturers WHERE name='%s'" % (manuname)
cur.execute(sql)
row = cur.fetchone()
supid = row[0] # gets the number
#print(supid)

mylines = []
with open(input_name,"r") as fi:
    for line in fi:
        mylines.append(line)
        #print(mylines)
        if line == '$$$$\n':
          # if it's not a header line, name = catalog number = SPHxxxxx
          name = mylines[0].rstrip()
          # Get compound ID
          sql = "Select id from Compounds where catn='%s' and ManuID='%s'" % (name,supid)
          cur.execute(sql)
          row = cur.fetchone()
          cid = row[0]
          t1 = ''.join(mylines)
          b1 = base64.b64encode(t1.encode('utf-8'))
          # insert the cid and base64 encoded text into the Molecules table
          sql = f"insert into Molecules (cid,molecule) values ({cid},'{b1.decode()}')"
          #print(cid)
          cur.execute(sql)
          mylines = []
con.commit()
con.close()

