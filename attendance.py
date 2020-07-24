import psycopg2



roll_no = int(input("Enter the roll number of student to calculate attendance : "))
sub_code = input("enter subject code : ")


connection = psycopg2.connect(user = "srajika",
                                      password = "12345",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "mydb")
cursor = connection.cursor()



query = "SELECT count(DISTINCT pdate) from attendance where sub_code = '" + str(sub_code) + "';"
cursor.execute(query)
days = cursor.fetchone()

query = "select count(*) from attendance where sub_code = '" + str(sub_code) + "' AND roll_no = '" +str(roll_no)+ "';"
cursor.execute(query)
attn = cursor.fetchone()

# print(days)
# print(attn)

percent = (attn[0]*100)/days[0]
print(percent)
	

if(connection):
	cursor.close()
	connection.close()
	print("PostgreSQL connection is closed")