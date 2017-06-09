import mysql.connector
Con = mysql.connector.connect(host="127.0.0.1", port=3306, user="root", passwd="hussain", db="user")
cursor=Con.cursor()
#Another Method if ID=int(raw_input("Enter your ID:")) then convert SQL to like "str(+ID)")
ID=raw_input("Enter Your ID:")
NAME=raw_input("Enter Your Name:")
EMAIL=raw_input("Enter Your Email:")
SALARY=raw_input("Enter Your Salary:")
PHONE=raw_input("Enter Your Phone Number:")
ADDRESS=raw_input("Enter Your Address:")
SQL=("insert into user values("+ID+",'"+NAME+"','"+EMAIL+"',"+SALARY+","+PHONE+",'"+ADDRESS+"')")
cursor.execute(SQL)
print "one Row inserted Sucessfully"
Con.commit()
cursor.close()
Con.close()


