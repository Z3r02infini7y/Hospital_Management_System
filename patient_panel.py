def patient():
    import sqlite3
    con=sqlite3.connect("HMS.db")
    mycursor=con.cursor()
    query="select p_id from registration"
    mycursor.execute(query)
    records=mycursor.fetchall()
    u1=input("enter your P_ID:")
    u=int(u1)
    if u==records[u][0]:  
        k=0
        while k<6:   
                print("(1) Patient's Details")
                print("(2) Patient's Current illness")
                print("(3) Doctors Involved")
                print("(4) Test Reports")
                print("(5) Billing Information")
                print("(6) Go Back")
                user3=int(input("enter your choice:"))
                if user3==1:
                    query="select * from registration"
                    mycursor.execute(query)
                    records=mycursor.fetchall()
                    print("\n")
                    print("P_DETAILS(Name,Phone_no,City,P_id) = ",records[u],"\n")
                elif user3==2:
                    query="select * from illness"
                    mycursor.execute(query)
                    records=mycursor.fetchall()
                    print("\n")
                    print("C_illness = ",records[u][0],"\n")
                elif user3==3:
                    query="select doctors, specialist from doctors"
                    mycursor.execute(query)
                    records=mycursor.fetchall()
                    print("\n")
                    print("Doctors Involved(Name,Qualifications):",records[u],"\n")
                elif user3==4:
                    query="select * from condition where p_id="+u1
                    mycursor.execute(query)
                    records=mycursor.fetchall()
                    print("\n")
                    print("Test Report is:\n",records[0][0:4])
                elif user3==5:
                    print("\n('Medicine_bought',Price,Quantity,P_ID,'P_name',P_mobile,'P_city')")
                    query="select * from p_medicine where p_id="+str(u1)
                    mycursor.execute(query)
                    records=mycursor.fetchall()
                    print("\n")
                    print(records[0])
                    print("\n")
                elif user3==6:
                    break
    else:
        print("Invalid P_ID..YA..HA..")