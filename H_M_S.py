import sqlite3
con=sqlite3.connect("HMS.db")
mycursor=con.cursor()
import billing_panel as bp
import patient_panel as pp
print("**********************************************************************")
print("**                                                                  **")
print("**                WELCOME TO HOSPITAL MANAGEMENT SYSTEM             **")
print("**                                                                  **")
print("**********************************************************************\t\t\t\t\t\t\t\t\t\t\tcreated by: Sarpreet Singh_a student at BBSBEC")
value=int(0)
while value<3:
    print("                        (1) For Patient Panel                     ")
    print("                        (2) For Reception Panel                   ")
    print("                        (3) For Billing Panel                     ")
    print("                        (4) Exit                                  ")
    user = int(input("Enter Your Choice:"))
    if user==1:
        pp.patient()
    elif user==2:
        j=0
        while j<6:  
            print("(1) Registration")
            print("(2) Medical Matter Management")
            print("(3) Go Back")
            user1=int(input("enter your choice:"))
            if user1==1:
                t=0
                while t<3:    
                    print("\n\n(1) Add Patient Data")
                    print("(2) Display All Records")
                    print("(3) Delete Patient Data")
                    print("(4) Delete Billing Data")
                    print("(5) Go Back")
                    user4=int(input("Enter Your Choice:"))
                    if user4==1:
                        print("Start Of P_id's is 0\n")
                        p_name=input("enter patient's name:")
                        p_mobile=input("enter patient's contact no:")
                        p_city=input("enter patient's city:")
                        p_id=input("enter patient's ID:")
                        #insert into table(a1,a2,a3,a4) values('v1',v2,'v3',v4)
                        query="insert into registration(p_name,p_mobile,p_city,p_id) values('"+p_name+"',"+p_mobile+",'"+p_city+"',"+p_id+")"
                        con.execute(query)
                        con.commit()
                        print("\nWhat is your reason of Visiting ?\n")
                        print("(1) Eyes checkup\n(2) X-ray Scan\n(3) Common Disease\n(4) Child Checkup\n(5) Cancer Treatment\n(6) Emergency Case\n(7) Surgery Case" )
                        u=int(input("enter your choice:"))
                        if u==1:
                            query="select wards from wards where w_id=1"
                            mycursor.execute(query)
                            records=mycursor.fetchall()
                            print(str(records[0][0]))
                            a="Eyes Related Issues"
                            query2="insert into illness(c_illness,p_id) values('"+a+"',"+p_id+")"
                            con.execute(query2)
                            con.commit()
                            d="Dr. Ravi Kumar Shukla"
                            s="M.D/M.S/M.B.B.S"
                            query3="insert into doctors(doctors,specialist,p_id) values('"+d+"','"+s+"',"+p_id+")"
                            con.execute(query3)
                            con.commit()
                        elif u==2:
                            query="select wards from wards where w_id=2"
                            mycursor.execute(query)
                            records=mycursor.fetchall()
                            print(str(records[0][0]))
                            b="X-Rays Scan"
                            query2="insert into illness(c_illness,p_id) values('"+b+"',"+p_id+")"
                            con.execute(query2)
                            con.commit()
                            d="Sanjeev Arora"
                            s="D.R Degree"
                            query3="insert into doctors(doctors,specialist,p_id) values('"+d+"','"+s+"',"+p_id+")"
                            con.execute(query3)
                            con.commit()
                        elif u==3:
                            query="select wards from wards where w_id=3"
                            mycursor.execute(query)
                            records=mycursor.fetchall()
                            print(str(records[0][0]))
                            c="Common Disease(cough,fever,cold..etc..)"
                            query2="insert into illness(c_illness,p_id) values('"+c+"',"+p_id+")"
                            con.execute(query2)
                            con.commit()
                            d="Dr. Ashok Rajgopal"
                            s="M.D/M.M"
                            query3="insert into doctors(doctors,specialist,p_id) values('"+d+"','"+s+"',"+p_id+")"
                            con.execute(query3)
                            con.commit()
                        elif u==4:
                            query="select wards from wards where w_id=4"
                            mycursor.execute(query)
                            records=mycursor.fetchall()
                            print(str(records[0][0]))
                            d="child checkup"
                            query2="insert into illness(c_illness,p_id) values('"+d+"',"+p_id+")"
                            con.execute(query2)
                            con.commit()
                            d="Dr. Ram Nath Chopra"
                            s="M.B.B.S"
                            query3="insert into doctors(doctors,specialist,p_id) values('"+d+"','"+s+"',"+p_id+")"
                            con.execute(query3)
                            con.commit()
                        elif u==5:
                            query="select wards from wards where w_id=5"
                            mycursor.execute(query)
                            records=mycursor.fetchall()
                            print(str(records[0][0]))
                            e="cancer related issues"
                            query2="insert into illness(c_illness,p_id) values('"+e+"',"+p_id+")"
                            con.execute(query2)
                            con.commit()
                            d="Dr. Satya Paul Agarwal"
                            s="M.B.B.S/M.D/M.Ch/M.D-PhD"
                            query3="insert into doctors(doctors,specialist,p_id) values('"+d+"','"+s+"',"+p_id+")"
                            con.execute(query3)
                            con.commit()
                        elif u==6:
                            query="select wards from wards where w_id=6"
                            mycursor.execute(query)
                            records=mycursor.fetchall()
                            print(str(records[0][0]))
                            f="Emergency(Bleeding,Breathing Issue,Severe Damage..etc..)"
                            query2="insert into illness(c_illness,p_id) values('"+f+"',"+p_id+")"
                            con.execute(query2)
                            con.commit()
                            d="Dr. Jasbir Singh Bajaj"
                            s="S.M/M.B.B.S"
                            query3="insert into doctors(doctors,specialist,p_id) values('"+d+"','"+s+"',"+p_id+")"
                            con.execute(query3)
                            con.commit()
                        elif u==7:
                            query="select wards from wards where w_id=7"
                            mycursor.execute(query)
                            records=mycursor.fetchall()
                            print(str(records[0][0]))
                            g="Surgery"
                            query2="insert into illness(c_illness,p_id) values('"+g+"',"+p_id+")"
                            con.execute(query2)
                            con.commit()
                            d="Dr. Mukesh Batra"
                            s="M.B.B.S/S.M/M.D-PhD"
                            query3="insert into doctors(doctors,specialist,p_id) values('"+d+"','"+s+"',"+p_id+")"
                            con.execute(query3)
                            con.commit()
                        else:
                            print("Invalid Option...YA..HA..")
                        print("\n Data recorded Successfully..\n")
                    elif user4==2:
                        query2="select * from registration"
                        mycursor.execute(query2)
                        records=mycursor.fetchall()
                        print("\nPatient(s) Personal Information:\n")
                        for row in records:
                            print("P_NAME = ",row[0])
                            print("P_MOBILE = ",row[1])
                            print("P_CITY = ",row[2])
                            print("P_ID = ",row[3],"\n")
                        print("\nPatient(s) Current Illness:")
                        query3="select * from illness"
                        mycursor.execute(query3)
                        records=mycursor.fetchall()
                        print("\n")
                        for row in records:
                            print("C_illness = ",row[0])
                            print("P_id = ",row[1])
                        print("\nAssigned Doctor(s):")
                        query4="select * from doctors"
                        mycursor.execute(query4)
                        records=mycursor.fetchall()
                        print("\n")
                        for row in records:
                            print("Doctor Name = ",row[0])
                            print("Specialist = ",row[1])
                            print("P_id = ",row[2],"\n")
                        print("\nHealth Status:\n")
                        query5="select * from condition"
                        mycursor.execute(query5)
                        records=mycursor.fetchall()
                        for row in records:
                            print("P_Name:",row[5])
                            print("P_ID:",row[4])
                            print("Condition:",row[0],row[1],row[2],row[3],"\n")
                        print("\nBilling Information:\n")
                        query6="select * from p_medicine"
                        mycursor.execute(query6)
                        records=mycursor.fetchall()
                        for row in records:
                            print("P_ID:",row[3])
                            print("P_Name:",row[4])
                            print("P_Mobile:",row[5])
                            print("P_City:",row[6])
                            print("M_Bought:",row[0])
                            print("Quantity",row[2])
                            print("Total_Price: Rs.",row[1],"\n")
                    elif user4==3:
                        user=input("enter patient ID to delete:")
                        query3='DELETE FROM registration WHERE p_id='+user    
                        mycursor.execute(query3)
                        con.commit()
                        query4='DELETE FROM illness WHERE p_id='+user
                        mycursor.execute(query4)
                        con.commit()
                        query4="DELETE FROM doctors WHERE p_id="+user
                        mycursor.execute(query4)
                        con.commit()
                        query5="DELETE FROM condition WHERE p_id="+user
                        con.execute(query5)
                        con.commit()
                        print(mycursor.rowcount, "\nrecord deleted \n")
                    elif user4==4:
                        user1=input("enter patient ID to delete his/her Billing Data:")
                        query6='DELETE FROM p_medicine WHERE p_id='+user1
                        con.execute(query6)
                        con.commit()
                        print("\nData Deleted Successfully..\n")
                    elif user4==5:
                        break
                    else:
                        print("Invalid Option.....YA-HA...")
                        break  
            elif user1==2:
                t2=0
                while t2<10:    
                    print("(1) Generate Report")
                    print("(2) Go Back")
                    user6=int(input("Enter Your Choice:"))
                    if user6==1:
                        us3r1=input("enter patient name:")
                        us3r2=int(input("enter patient ID:"))
                        us3r3=str(us3r2)
                        query="select p_name, p_id from registration"
                        mycursor.execute(query)
                        records=mycursor.fetchall()
                        try:
                            if us3r1==records[us3r2][0]:
                                if us3r2==records[us3r2][1]:
                                    print("patient name is: ",records[us3r2][0])
                                    print("and patient's condition is:")
                                    print("(1) Very Good")
                                    print("(2) Good")
                                    print("(3) Bad")
                                    print("(4) Severe")
                                    print("(5) Go Back")
                                    us3r=int(input("enter your choice:"))
                                    if us3r==1:
                                        a="Your condition is Very Good. You can leave the Hospital.ThankYou.."
                                        b="*"
                                        c="*"
                                        d="*"
                                        query="insert into condition(very_good,good,bad,severe,p_name,p_id) values('"+a+"','"+b+"','"+c+"','"+d+"','"+us3r1+"',"+us3r3+")"
                                        con.execute(query)
                                        con.commit()
                                        query1="select very_good from condition"
                                        mycursor.execute(query1)
                                        records=mycursor.fetchall()
                                        print(str(us3r1)+"'s Condition is:",records[us3r2][0])
                                        print("\nReport generated successfully..")
                                    elif us3r==2:
                                        a="*"
                                        b="Your Condition is Good. You can leave the hospital, But you need to take rest for some days and take the necessary precautions."
                                        c="*"
                                        d="*"
                                        query="insert into condition(very_good,good,bad,severe,p_name,p_id) values('"+a+"','"+b+"','"+c+"','"+d+"','"+us3r1+"',"+us3r3+")"
                                        con.execute(query)
                                        con.commit()
                                        query1="select good from condition"
                                        mycursor.execute(query1)
                                        records=mycursor.fetchall()
                                        print(str(us3r1)+"'s Condition is:",records[us3r2][0])
                                        print("\nReport generated successfully..")
                                    elif us3r==3:
                                        a="*"
                                        b="*"
                                        c="Your condition is Bad. you need to follow the instructions of your assigned doctor. you need rest, proper food and medicine at regular intervals. (The Hospital advices you to admit in the Hospital)"
                                        d="*"
                                        query="insert into condition(very_good,good,bad,severe,p_name,p_id) values('"+a+"','"+b+"','"+c+"','"+d+"','"+us3r1+"',"+us3r3+")"
                                        con.execute(query)
                                        con.commit()
                                        query1="select bad from condition"
                                        mycursor.execute(query1)
                                        records=mycursor.fetchall()
                                        print(str(us3r1)+"'s Condition is:",records[us3r2][0])
                                        print("\nReport generated successfully..")
                                    elif us3r==4:
                                        a="*"
                                        b="*"
                                        c="*"
                                        d="Patient(s) condition is worse. patient is in danger state. Need 24-hour Care."
                                        query="insert into condition(very_good,good,bad,severe,p_name,p_id) values('"+a+"','"+b+"','"+c+"','"+d+"','"+us3r1+"',"+us3r3+")"
                                        con.execute(query)
                                        con.commit()
                                        query1="select severe from condition"
                                        mycursor.execute(query1)
                                        records=mycursor.fetchall()
                                        print(str(us3r1)+"'s Condition is:",records[us3r2][0])
                                        print("\nReport generated successfully..")
                                    elif us3r==5:
                                        break
                            else:
                                print("Invalid Name..YA..HA..")
                        except IndexError:
                            print("Invalid P_ID..YA..HA..")
                    elif user6==2:
                            break
                    else:
                        print("Invalid Option..YA..HA..")
                        break
            elif user1==3:
                break
            else:
                print("Invalid Option.....YA-HA...")
                break
    elif user==3:
        query="select username, password from security where id=1"
        mycursor.execute(query)
        records=mycursor.fetchall()
        u=input("enter username:")
        p=input("enter password:")
        if u==records[0][0] and p==records[0][1]:
            bp.billing()
        else:
            print("\nYour Username or Password is Incorrect..YA..HA..\n")
    elif user==4:
        print("\nThankyou for using my System \n")
        break
    else:
        print("Invalid Option.....YA-HA...")
        break