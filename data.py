import MySQLdb
SQL="select * from User"
Con = MySQLdb.Connect(host="127.0.0.1", port=3306, user="root", passwd="hussain", db="user")
cursor=Con.cursor()
cursor.execute(SQL)
data=cursor.fetchall()
for rows in data:
    print rows
    
    # if you want in json format then follow below step
import json
json_output=json.dumps(data)
print(json_output)
    
