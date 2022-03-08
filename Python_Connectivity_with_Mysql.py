import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="assignment5"
    )

user_input=''
while user_input!=5:

    print('''
''')
    print('''choices
             1.start entering data
             2.delete the rollno
             3.show all data
             4. update data
             5. exit''')

    mycursor=mydb.cursor()

    user_input=int(input("enter your choice"))

    if user_input==1:

        a=int(input("enter your rollno"))
        b=input("enter your name")
        c=input("enter your address")

        my="INSERT INTO info(rollno,name,address) VALUES(%s,%s,%s)"
        x=(a,b,c)

        mycursor.execute("SELECT *FROM info WHERE rollno={}" . format(a))
        myresult=mycursor.fetchall()

        for a in myresult:
            print()
        if a not in myresult:
            mycursor.execute(my,x)
            print(mycursor.rowcount,"record inserted")
            mydb.commit()
        else:
            print("data already exists ")

        mycursor.execute("SELECT *FROM info")
        result=mycursor.fetchall()
        print('''
''')


        for x in myresult:
            print(x)


    elif user_input==2:
        k=int(input("enter rollno of which you want to delete data"))
        r=input("are you sure y/n")
        
        if r=='y':
            mycursor.execute("SELECT *FROM info WHERE rollno={}". format(k))
            yup=mycursor.fetchall()
            row = ''
            for row in yup:
                mycursor.execute("DELETE FROM info WHERE rollno = {}". format(k))
                mydb.commit()
                print("deleted")
                if row not  in yup:
                    print("data doesnot exist")
        else:
            print("ok")

    elif user_input==3:
        
        
        mycursor.execute("SELECT *FROM info")
        myresult=mycursor.fetchall()
        
        for row in myresult:
             print(row)

    elif user_input==4:
        r=int(input("enter the rollno you want to update"))
        k=input("are you sure to update y/n")

        if k=='y':
            mycursor.execute("SELECT *FROM info WHERE rollno={}". format(r))
            yes=mycursor.fetchall()
            
            for k in yes:
                print(k)
                q=input("name")
                w=input("address")

                mycursor.execute("UPDATE INFO SET name = %s WHERE rollno = %s",(q,r))
                mycursor.execute("UPDATE INFO SET address = %s WHERE rollno = %s",(w,r))
                mydb.commit()
                print(mycursor.rowcount,"record update")
            if not k in yes:
                print("data doesn't exists")
    
        else:
            print("data is not updated")

    elif user_input==5:
        print("bye")
        quit()
      

            

    



  

        
