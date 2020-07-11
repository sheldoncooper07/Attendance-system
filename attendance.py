import csv

roll_no = int(input("Enter the roll number of student to calculate attendance : "))

nodays = 0
dys = []
attn = 0
with open('attendance.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # print(row[0])
        # print(row[1])

        if(row[0] not in dys):
            dys.append(row[0])
            nodays += 1
        if(int(row[1]) == roll_no):
            attn += 1

     

# print(nodays)
# print(attn)

percent = (attn*100)/nodays

print(percent)

