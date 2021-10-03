def billing():
    
    import sqlite3
    con=sqlite3.connect("HMS.db")
    mycursor=con.cursor()
    query1="select m_id from medicine"
    mycursor.execute(query1)
    records=mycursor.fetchall()
    print("\nmedicine name:\t\t\t\t\t\tmedicine ID:\n\n")
    for i in records:  
        l=i[0]
        query="select m_name, m_id from medicine where m_id="+str(l)
        mycursor.execute(query)
        records1=mycursor.fetchall()
        s=str(records1[0][0])
        r=str(records1[0][1])
        print(s.ljust(45,"-"),r)
    query="select m_name, m_id from medicine"
    mycursor.execute(query)
    records1=mycursor.fetchall()
    input("enter medicine name:")
    d=int(input("enter medicine id:"))
    d1=str(d) 
    try:  
        if d==records1[d][1]:    
            dd=records1[d][0]
            print(dd)
            query="select price_unit, price_strip from medicine where m_id="+d1
            mycursor.execute(query)
            records=mycursor.fetchall()
            print("Medicine price(per unit):\t\t\t\t\tMedicine Price(per strip): ")
            print("Rs.",records[0][0],"\t\t\t\t\t\t\t\t   ","Rs.",records[0][1])
            user=input("\nDo you want to buy it ?(Yes/No)\n")
            if user=="yes" or user=="Yes" or user=="YES":
                q2=str(input("enter your P_ID:"))
                query1="select quantity from medicine where m_id="+d1
                mycursor.execute(query1)
                records1=mycursor.fetchall()
                if records1[0][0]!=0:  
                    print("we currently have",records1[0][0],"packs in stock. How many do you want to buy ?")
                    user1=int(input())
                    r=user1*records[0][1]
                    print("that'll be: Rs.",r,"Only")
                    print("Thankyu. we wish for your Good Health.")
                    q=int(records1[0][0])-user1
                    q1=str(q)
                    query2="update medicine set quantity='"+q1+"'where m_id="+d1
                    con.execute(query2)
                    con.commit()
                    query6="select * from registration where p_id="+q2
                    mycursor.execute(query6)
                    records6=mycursor.fetchall()
                    query7="insert into p_medicine(p_id,p_name,p_mobile,p_city,m_bought,price,quantity) values('"+str(records6[0][3])+"','"+str(records6[0][0])+"','"+str(records6[0][1])+"','"+str(records6[0][2])+"','"+str(dd)+"','"+str(r)+"','"+str(user1)+"')"
                    con.execute(query7)
                    con.commit()
                    print(" \nData Updated Successfully..\n")
                else:
                    print("sorry, we are currently out of stock.")
            elif user=="no" or user=="NO" or user=="No":
                print("Thankyu. we wish for your Good Health.")
            else:
                print("Invalid option..YA..HA..")
    except IndexError:
        print("Medicine Not Available")