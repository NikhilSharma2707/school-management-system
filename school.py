import pandas as pd


#SOURCE CODE FOR SCHOOL MANAGEMENT
print("""


╔------------------------------------------------------╗

|=================================================
=====|
|=██▓▒░ ►▬ WELCOME TO SCHOOL MANAGMENT SYSTEM
▬◄ ░▒▓██=|

|=================================================
=====|
╚------------------------------------------------------╝


""")


#CREATING DATABASE IN MYSQL


import mysql.connector




 
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists pyschool")
mycursor.execute("use pyschool")

#CREATING REQUIRED TABLES


mycursor.execute("create table if not exists pystudent(name varchar(50) not null,class varchar(25) not null,roll varchar(5) primary key,gender varchar(8),mobile_number varchar(10) not null,email varchar(40) not null,city varchar(20) not null)")


mycursor.execute("create table if not exists pystaff(staff_id varchar(5) primary key,name varchar(50) not null,gender varchar(8),subject varchar(25) not null,Salary varchar(5),mobile_number varchar(10) not null,email varchar(40) not null,city varchar(10) not null )")



mycursor.execute (" create table if not exists fee (roll varchar(5) references pystudent(roll), FeeDeposit varchar(6) NOT NULL, month varchar(10) NOT NULL)")
mydb.commit()

 


while(True):


print("1~ADD NEW STUDENT")
print("	")
print("2~ADD NEW STAFF")
print("	")
print("3~SEARCH STUDENT BY ROLL.NO")
print("	")
print("4~SEARCH STUDENT BY NAME")
print("	")
print("5~SEARCH STUDENT BY CITY")
print("	")
print("6~SEARCH STAFF BY STAFFID")
print("	")
print("7~SEARCH STAFF BY STAFF'S NAME")
print("	")
print("8~SEARCH STAFF BY STAFF'S CITY")
print("	")
print("9~DISPLAYING STUDENT OF CLASS 12 ")

 
print("	")
print("10~DISPLAYING STUDENT OF CLASS 11 ")
print("	")
print("11~UPDATING STUDENT RECORD")
print("	")
print("12~UPDATING STUDENT'S ADDRESS")
print("	")
print("13~UPDATING STUDENT'S MOBILE NUMBER")
print("	")
print("14~UPDATING STUDENT'S EMAIL")
print("	")
print("15~UPDATING STAFF RECORD")
print("	")
print("16~REMOVE STUDENT")
print("	")
print("17~REMOVE STAFF")
print("	")
print("18~TO DELETE ALL RECORDS")
print("	")
print("19~TO DEPOSIT FEE OF STUDENT")

 
print("	")
print("20~TO VIEW FEE OF ANY STUDENT")
print("	")
print("21~EXIT SOFTWARE")
print("	")

print("++++++++++++++++++++++++++++++++++++++++++++++++")

print("	")
ch=int(input("ENTER YOUR CHOICE:~"))



#PROCEDURE FOR Entering A NEW Student Record


if(ch==1):
print("	")
print("======【ALL FIEDS MARKED (*) ARE MANDATORY TO BE FILLED】======")
print("	")
name=input("ENTER STUDENT'S NAME*:~") print("	")
 
classs=str(input("ENTER STUDENT'S CLASS*:~")) print("	")
roll=str(input("ENTER STUDENT'S ROLL NO*:~")) print("	")
gender=str(input("ENTER GENDER:~")) print("	")
mobile_number=str(input("ENTER STUDENT'S MOBILE NUMBER*:~"))
if len(mobile_number)!=10:
print("NUMBER IS NOT VALID(ENTER A 10 DIGIT NUMBER)")
print("	")
mobile_number=str(input("ENTER STUDENT'S MOBILE NUMBER*:~"))
print("	")
email=input("ENTER STUDENT'S EMAIL ID*:~") print("	")
city=input("ENTER STUDENT'S ADDRESS*:~")
print("	")
mycursor.execute(f"insert into pystudent values('{name}','{classs}','{roll}','{gender}','{mobile_number}','{ema il}','{city}')")
 
mydb.commit()
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 100%")
print("	")
print("+++++++++++++++++++Student record has been saved successfully!!++++++++++++++++++")


#PROCEDURE FOR Entering A New Staff Record


elif(ch==2):
print("	")
print("======【ALL FIELDS MARKED (*) ARE MANDATORY TO BE FILLED】======")
print("	")
sid=input("ENTER STAFF ID*:~") print("	")
sname=input("ENTER STAFF'S NAME*:~") print("	")
gender=input("ENTER GENDER:~") print("	")
dep=input("ENTER DEPARTMENT OR SUBJECT*:~")

 
print("	")
salary=input("ENTER SALARY:~") print("	")
mobile_number=input("ENTER STAFF'S MOBILE NUMBER*:~")
if len(mobile_number)!=10:
print("NUMBER IS NOT VALID(ENTER A 10 DIGIT NUMBER)")
print("	")
mobile_number=input("ENTER STAFF'S MOBILE NUMBER*:~")
print("	")
email=input("ENTER STAFF'S EMAIL ID*:~") print("	")
city=input("ENTER STAFF'S ADDRESS*:~") print("	")
mycursor.execute(f"insert into pystaff values('{sid}','{sname}','{gender}','{dep}','{salary}','{mobile_number}','{email}','{city}')")
mydb.commit()
print("	")



 
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 100%")
print("	")
print("+++++++++++++++Staff record has been saved successfully!!!+++++++++++++++++")


#PROCEDURE FOR displaying STUDENT RECORD BY ROLLNO.


elif(ch==3):
print("	")
roll_no=str(input("ENTER STUDENT'S ROLL NUMBER:")) print("	")
mycursor.execute("select * from pystudent where roll='"+roll_no+"'")
for i in mycursor: name,classs,roll_no,gender,mobile_number,email,address=i print(f'NAME:~ {name}')
print("	")
print(f'CLASS:~ {classs}') print("	")

 
print(f'ROLL NUMBER:~ {roll_no}') print("	")
print(f'GENDER:~ {gender}') print("	")
print(f'MOBILE_NUMBER:~ {mobile_number}') print("	")
print(f'EMAIL ID:~ {email}') print("	")
print(f'ADDRESS:~ {address}') print("	")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 100%")
print("	")
print("+++++++++++++++ STUDENT DATA HAS BEEN SUCCESSFULLY SHOWN!!!+++++++++++++++++")



#DIPPLAY STUDENT RECORD BY NAME
elif(ch==4):
print("	")
name=str(input("ENTER STUDENT'S NAME:~"))

 
print("	")
mycursor.execute("select * from pystudent where name='"+name+"'")
for i in mycursor: name,classs,roll_no,gender,mobile_number,email,address=i print(f'NAME:~ {name}')
print("	")
print(f'CLASS:~ {classs}') print("	")
print(f'ROLL NUMBER:~ {roll_no}') print("	")
print(f'GENDER:~ {gender}') print("	")
print(f'MOBILE_NUMBER:~ {mobile_number}') print("	")
print(f'EMAIL ID:~ {email}') print("	")
print(f'ADDRESS:~ {address}') print("	")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 100%")
 
print("	")
print("+++++++++++++++ STUDENT DATA HAS BEEN SUCCESSFULLY SHOWN!!!+++++++++++++++++")


#DISPLAY STUDENT RECORD BY CITY
elif(ch==5):
print("	")
city=input("ENTER STUDENT'S CITY:")
print("	")
mycursor.execute("select * from pystudent where city='"+city+"'")
for i in mycursor: name,classs,roll_no,gender,mobile_number,email,address=i print(f'NAME:~ {name}')
print("	")
print(f'CLASS:~ {classs}') print("	")
print(f'ROLL NUMBER:~ {roll_no}') print("	")
print(f'GENDER:~ {gender}') print("	")
 
print(f'MOBILE_NUMBER:~ {mobile_number}') print("	")
print(f'EMAIL ID:~ {email}') print("	")
print(f'ADDRESS:~ {address}') print("	")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 100%")
print("	")
print("+++++++++++++++ STUDENT DATA HAS BEEN SUCCESSFULLY SHOWN!!!+++++++++++++++++")


#PROCEDURE FOR DISPLAYING STAFF RECORD BY STAFFID


elif(ch==6):
print("	")
sid=str(input("ENTER STAFF ID:~")) print("	")
mycursor.execute(f"select * from pystaff where staff_id='{sid}'") data4 = mycursor.fetchall()
 
df4 = pd.DataFrame(data4,columns=["STAFFID","NAME","GENDER", "SUBJECT","SALARY","MOBILE    NUMBER","EMAIL","CITY"])
print(df4)
print("	")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 100%")
print("	")
print("+++++++++++++++ STAFF DATA HAS BEEN SUCCESSFULLY SHOWN!!!+++++++++++++++++")



#DISPLAY STAFF RECORD BY NAME
elif(ch==7):
print("	")
name=input("ENTER STAFF NAME:~") print("	")
mycursor.execute(f"select * from pystaff where name='{name}'")
data5 = mycursor.fetchall()




 
df5 = pd.DataFrame(data5,columns=["STAFFID","NAME","GENDER", "SUBJECT","SALARY","MOBILE    NUMBER","EMAIL","CITY"])
print(df5)
print("	")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 100%")
print("	")
print("+++++++++++++++ STAFF DATA HAS BEEN SUCCESSFULLY SHOWN!!!+++++++++++++++++")
print("	")





#DISPLAY STAFF RECORD BY CITY



elif(ch==8):
print("	")
city=input("ENTER STAFF CITY:~") print("	")
 
mycursor.execute("select * from pystaff where city='"+city+"'") data6 = mycursor.fetchall()
df6 = pd.DataFrame(data6,columns=["STAFFID","NAME","GENDER", "SUBJECT","SALARY","MOBILE    NUMBER","EMAIL","CITY"])
print(df6)
print("	")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 100%")
print("	")
print("+++++++++++++++ STAFF DATA HAS BEEN SUCCESSFULLY SHOWN!!!+++++++++++++++++")
print("	")


#PROCEDURE FOR DISPLAYING ALL STUDENTS of CLASS 12



elif(ch==9):
print("	")
print("	")

 
mycursor.execute("select * from pystudent where class=12") data1 = mycursor.fetchall()
df1 = pd.DataFrame(data1,columns=['NAME','CLASS','ROLLNO','GEN DER','MOBILENO','EMAIL','ADDRESS'])
print(df1)
print("	")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 100%") print("	")
print("+++++++++++++++ STUDENT DATA HAS BEEN SUCCESSFULLY SHOWN!!!+++++++++++++++++")


# PROCEDURE FOR DISPLAYING ALL STUDENTS of CLASS 11


elif(ch==10):
print("	")
print("	")
mycursor.execute("select * from pystudent where class=11") data2 = mycursor.fetchall()




 
df2 = pd.DataFrame(data2,columns=['NAME','CLASS','ROLLNO','GEN DER','MOBILENO','EMAIL','ADDRESS'])
print(df2)
print("	")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 100%") print("	")
print("+++++++++++++++ STUDENT DATA HAS BEEN SUCCESSFULLY SHOWN!!!+++++++++++++++++")



#UPDATING STUDENT RECORD


elif(ch==11):
print("	")
roll=str(input("ENTER STUDENT'S ROLL NO. WHOSE RECORD IS TO BE UPDATED:~"))
print("	")
name=input("ENTER STUDENT'S NAME*:~") print("	")
classs=str(input("ENTER STUDENT'S CLASS*:~"))


 
print("	")
rollno=str(input("ENTER STUDENT'S ROLL NO*:~")) print("	")
gender=str(input("ENTER GENDER:~")) print("	")
mobno=str(input("ENTER STUDENT'S MOBILE NUMBER*:~"))
if len(mobno)!=10:
print("NUMBER IS NOT VALID(ENTER A 10 DIGIT NUMBER)")
print("	")
mobno=str(input("ENTER STUDENT'S MOBILE NUMBER*:~"))
print("	")
email=input("ENTER STUDENT'S EMAIL ID*:~") print("	")
city=input("ENTER STUDENT'S ADDRESS*:~")
print("	")
update=f"update pystudent set name='{name}',class='{classs}',roll='{rollno}',gender='{gender}',mo bile_number='{mobno}',email='{email}',city='{city}' where roll='{roll}'"

 
mycursor.execute(update) mydb.commit()
print("	")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 100%")
print("	")
print("+++++++++++++++ STUDENT RECORD IS UPDATED SUCESSFULLY!!!+++++++++++++++++")
print("	")
#UPDATING STUDENT ADDRESS


elif(ch==12):
print("	")
rollno=str(input("ENTER STUDENT'S ROLL NO. WHOSE ADDRESS IS TO BE UPDATED:~"))
print("	")
city=input("ENTER STUDENT'S NEW ADDRESS*:~")
print("	")
mycursor.execute(f"update pystudent set city='{city}' where roll='{rollno}'")
mydb.commit()


 
print("	")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 100%")
print("	")
print("+++++++++++++++ STUDENT RECORD IS UPDATED SUCESSFULLY!!!+++++++++++++++++")
print("	")



#UPDATING STUDENT MOBILE NUMBER



elif(ch==13):
print("	")
roll=str(input("ENTER STUDENT'S ROLL NO. WHOSE MOBILE NUMBER IS TO BE UPDATED:~"))
print("	")
mobno=str(input("ENTER STUDENT'S MOBILE NUMBER*:~"))
if len(mobno)!=10:
print("NUMBER IS NOT VALID(ENTER A 10 DIGIT NUMBER)")
 
print("	")
mobno=str(input("ENTER STUDENT'S MOBILE NUMBER*:~"))
print("	")
update=f"update pystudent set mobile_number='{mobno}' where roll='{roll}'"
mycursor.execute(update) mydb.commit()
print("	")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 100%")
print("	")
print("+++++++++++++++ STUDENT RECORD IS UPDATED SUCESSFULLY!!!+++++++++++++++++")
print("	")



#UPDATING STUDENT E-MAIL
elif(ch==14):
print("	")
roll=str(input("ENTER STUDENT'S ROLL NO. WHOSE EMAIL IS TO BE UPDATED:~"))
 
print("	")
email=str(input("ENTER STUDENT'S EMAIL:~")) print("	")
update=f"update pystudent set email='{email}' where roll='{roll}'"
mycursor.execute(update) mydb.commit()
print("	")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 100%")
print("	")
print("+++++++++++++++ STUDENT RECORD IS UPDATED SUCESSFULLY!!!+++++++++++++++++")
print("	")


#UPDATING STAFF RECORD
elif(ch==15):
print("	")
sidd=str(input("ENTER STAFF ID WHOSE RECORD IS TO BE UPDATED:~"))
print("	")


 
sname=input("ENTER STAFF'S NAME*:~") print("	")
sid=input("ENTER STAFF ID") print("	")
gender=input("ENTER GENDER:~") print("	")
dep=input("ENTER DEPARTMENT OR SUBJECT*:~")
print("	")
salary=input("ENTER SALARY:~") print("	")
mobile_number=input("ENTER STAFF'S MOBILE NUMBER*:~")
if len(mobile_number)!=10:
print("NUMBER IS NOT VALID(ENTER A 10 DIGIT NUMBER)")
print("	")
mobile_number=input("ENTER STAFF'S MOBILE NUMBER*:~")
print("	")
email=input("ENTER STAFF'S EMAIL ID*:~") print("	")
 
city=input("ENTER STAFF'S ADDRESS*:~") print("	")
update=f"update pystaff set staff_id='{sid}',name='{sname}',gender='{gender}',subject='{dep}',s alary='{salary}',mobile_number='{mobile_number}',email='{email}',city='{city}') where staff_id='{sidd}'" mycursor.execute(update) mydb.commit()
print("	")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 100%")
print("	")
print("+++++++++++++++Staff record has been saved successfully!!!+++++++++++++++++")


#PROCEDURE FOR DELETING STUDENT RECORD


elif(ch==16):
print("	")
r_no=str(input("ENTER STUDENT'S ROLL NO.:~")) print("	")


 
mycursor.execute("delete from pystudent where roll='"+r_no+"'")
mydb.commit()
print("	")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 100%")
print("	")
print("*++++++++++++++Student Record is successfully Deleted++++++++++++++")


#PROCEDURE FOR DELETING STAFF RECORD


elif(ch==17):
print("	")
sid=str(input("ENTER STAFF ID:~")) print("	")
mycursor.execute("delete from pystaff where staff_id='"+sid+"'")
 
print("	")
print("+++++++++++++++Staff Record is successfully Deleted++++++++++++++++")



#PROCEDURE FOR DELETING ALL RECORDS



elif(ch==18):
print("	")
delete=str(input("TYPE 'YES' TO CONFIRM:~")) print("	")
mycursor.execute("delete from pystudent") mydb.commit()
mycursor.execute("delete from pystaff") mydb.commit() mycursor.execute("delete from fee")
 
mydb.commit()
print("         ")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 100%")
print("	")
print("+++++++++++++++ALL RECORDS HAVE BEEN DELETED SUCESSFULLY++++++++++++++++")
print("	")



#PROCEDURE FOR DEPOSITING STUDENT'S FEES


elif(ch==19):
L=[]
roll=int(input("ENTER STUDENT'S ROLL NO.:~ ")) L.append(roll)
feedeposit=input("ENTER FEE AMOUNT TO BE DEPOSITED:~ ")
L.append(feedeposit)
month=input("ENTER MONTH OF FEE:~ ") L.append(month)
fee=(L)
sql="insert into fee (roll,feeDeposit,Month) values (%s,%s,%s)" mycursor.execute(sql,fee)
mydb.commit()

 
print("	")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 100%") print("	")



#PROCEDURE FOR VIEWING FEE OF ANY STUDENT
elif(ch==20):
print("	")
roll=input("ENTER STUDENT'S ROLL NO.:~ ")
print("	")
mycursor.execute("select sum(feedeposit) from fee where roll='"+roll+"'")
data3 = mycursor.fetchall()
df3 = pd.DataFrame(data3,index=['TOTAL FEE DEPOSITED IS:~ Rs'])
print(df3)
print("	")
mydb.commit()
print("	")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 100%") print("	")
 





#PROCEDURE TO EXIT SOFTWARE
elif(ch==21): print("	")
print("	O_|	")
print("	/|\	")
print("   / \     ") print("	")
print("	")
print("〣THANK YOU!〣") break
else:
print("	")
print("	")
print("《PLEASE ENTER VALID INPUT》")
print("	")
print("	")
