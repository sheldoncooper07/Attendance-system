import psycopg2

def insert(lst):
	connection = psycopg2.connect(user = "srajika",
                                      password = "12345",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "mydb")

	cursor = connection.cursor()
		
	print("connected")
	# query = "create table attendance (roll_no int, sub_code varchar(10), pdate date,primary key(roll_no,sub_code,pdate));"
	# cursor.execute(query)
	# print("table created")
	insert_statmnt = "insert into attendance(roll_no,sub_code,pdate) values(%s,%s,%s);"

	for tup in lst:
		try:
			cursor.execute(insert_statmnt,tup)
		except:
			cursor.execute("rollback;")


	
	connection.commit()
	
	if(connection):
	    cursor.close()
	    connection.close()
	    print("PostgreSQL connection is closed")
