import random
import pyautogui as auto
import webbrowser as wb
import pyperclip as pc
import pymysql as conn

# Personal PAssword Manager

confirm_input=auto.confirm(" 1 To Save The Password\n 2 To View Saved Password",buttons=['1','2'])

################################## Database Connection Part ##################################
db = conn.connect(host="Your Host",
                     user="root",
                     passwd="Your Password",
                     db="Database Name")

cur = db.cursor()
################################## Database Connection Part ##################################

if(confirm_input=="1"):
    Name=auto.prompt("Your Name")
    User_Name=auto.prompt("UserName/Email Address/Phone Number")
    Website_URL=auto.prompt("Website/App Name")
    Website_URL=Website_URL.lower()
    try:
        e=auto.confirm(" 1 To Generate A Strong Password\n 2 To Create Password Manually",buttons=["1","2"])

        if(e=="1"):
            a="abcdefghijklmnopqrstuvwxyz"
            b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            c="1234567890"
            d="!@#$%&*?~"

            length=8
            random_password="".join(random.sample(a+c+d+b, length))

            cnf=auto.confirm(random_password,"Your Password Is",buttons=['Copy','Exit'])
            if cnf=="Copy":
                pc.copy(random_password)
                auto.alert("Congratulations, Password Has Been Copied")

        ################################## Database Command Part ##################################
            command="Insert into User_Data (Name,User_Name,Password,URL) values(%s,%s,%s,%s)"
            value=(Name,User_Name,random_password,Website_URL)
            cur.execute(command,value)
            db.commit()
        ################################## Database Command Part ##################################

        elif(e=="2"):
            manually_password=auto.password("Enter The Password")
            cnf2=auto.confirm(manually_password,"Your Password Is",buttons=['Copy','Exit'])

            if cnf2=="Copy":
                pc.copy(manually_password)
                auto.alert("Congratulations, Password Has Been Copied")
        ################################## Database Command Part ##################################
            command="Insert into User_Data (Name,User_Name,Password,URL) values(%s,%s,%s,%s)"
            value=(Name,User_Name,manually_password,Website_URL)
            cur.execute(command,value)
            db.commit()
        ################################## Database Command Part ##################################
        auto.alert("Congratulations, Your Data Has Been Stored To Our Database ✅")
    except:
        auto.alert("User Name Already Exist")

if(confirm_input=="2"):
    Name=auto.prompt("Your Name")
    Website_URL=auto.prompt("Website/App Name")
    Website_URL=Website_URL.lower()
    ii=0
    try:
        ################################## Database Command Part ##################################
        command='Select * from User_Data where URL="'+Website_URL+'"and Name="'+Name+'"'
        cur.execute(command)
        for row in cur.fetchall():
            auto.alert("\n\tName = "+row[0]+"\t\n\n\tWebsite/App Name = "+row[3]+"\t\n\n\tUser Name = "+row[1]+"\t\n\n\tPassword = "+row[2])
            ii+=1
        ################################## Database Command Part ##################################
        if ii==0 :
            auto.alert("\t\n\tDetails Are Not Available  \t\n")
    except:
        auto.alert("\t\n\t Incorrect Website/App Name \t\n")
db.close()