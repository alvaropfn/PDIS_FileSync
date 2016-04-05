import sqlite3
import MySQLdb

#connection = sqlite3.connect("BDs/postgres.db")
connection = MySQLdb.connect("localhost", "alvaro", "q654321")

cursor = connection.cursor()

#cursor.execute("""DROP TABLE employee;""")

command = """
create table employee
(
	staff_number INTEGER PRIMARY KEY,
	fname VARCHAR(20),
	lname VARCHAR(30),
	gender CHAR(1),
	joining DATE,
	birth_date DATE
);
"""
cursor.execute(command)

command = """
insert into employee
(
	staff_number, fname, lname,
	gender, joining, birth_date
)
values
(
	NULL, "alvaro", "portela", "m", "2016-03-15","1985-12-03"
);
"""
cursor.execute(command)

command = """
insert into employee
(
	staff_number, fname, lname,
	gender, joining, birth_date
)
values
(
	NULL, "larissa", "coelho", "f", "2016-03-15","1991-11-22"
);
"""
cursor.execute(command)

command = "SELECT * FROM employee"

cursor.execute(command)
print("fetchall:")
result = cursor.fetchall()
for r in result:
	print(r)

print("==================")

cursor.execute(command)
print("\nfetch one:")
res = cursor.fetchone()
print(res)

connection.close()