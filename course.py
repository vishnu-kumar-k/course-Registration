import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1607",
    use_pure=True,
    database="project"
)
c=mydb.cursor()
def course_delete():
    course_view()
    print()
    c=mydb.cursor()
    s=input("Enter the course Id which need to be deleted....")
    c.execute("select * from course")
    con=0
    for i in c:
        if i[1]==s:
            con=1
    if con==0:
        print("NO Course id found......")
        print()
        course_delete()
        print()
    else:
        c.execute("delete from course where id=%s",(s,))
        print(" ******Deleted successfully **********   ")
        c.execute("commit")
        print()
def course_view():
    c=mydb.cursor()
    print()
    print("      ************** Course  ***********     ")
    t=0
    c.execute("select count(*) from course")
    for i in c:
        t=i[0]
    if t==0:
        print("No course add")
    else:    
        c.execute("select * from course")
        for i in c:
            print("NAME  :",i[0])
            print("ID  :",i[1])
        print()    
def ad_login():
    c=mydb.cursor()
    name=input("enter the name : ")
    pas=input("enter the password : ")
    c.execute("select * from admin")
    for i in c:
        n=i[0]
        l=i[1]
        if n==name or l==pas:
            return True
    return False
def ad_option():
    c=mydb.cursor()
    print("1.   Add new course  ")
    print("2.   view course   ")
    print("3.   Delete the course ")
    print("4.   Main Menu")
    print()
   
    t=input("Enter Your choice : ")
    if(t=="1"):
        e=input("Enter Course name : ")
        f=input("Enter Course id : ")
        h=input("Enter Course Duration : ")
        a=input("Enter Course Price : ")
        l=input("Enter the course Instrutor : ")
        c.execute("insert into course values(%s,%s,%s,%s,%s)",(e,f,h,a,l,))
        c.execute("commit")
        print("\n ---------Added successfully-------")
        ad_option()
    elif t=="2":
        course_view()
        ad_option()
    elif t=="3":
        course_delete()
        c.execute("commit")
        ad_option()
    else:
        main()
           
def admin():
    c=mydb.cursor()
    s=ad_login()
    if s==True:
        ad_option()
    else:
        print("You may entered wrong name or password")
        print("    OPTION    ")
        print("1.  Try Again")
        print("2.  Main Menu")
        s=input("Enter your choice  : ")
        print()
        if s=="1":
            admin()
        else:
            main()
#From here starts the User information--------------------
def mycourse(n):
    c=mydb.cursor()
    print("User Name : ",n)
    t=" select * from user_details where user_id= %s "
    n=(n,)
    c.execute(t,n)
    print("-------Mycourse-------")
    for i in c:
        print(i[0])
    c.close()
    user_choice(n)    
def course_view1():
    c=mydb.cursor()
    print()
    print("      ************** Course  ***********     ")
    c.execute("select * from course")
    for i in c:
        print("NAME  :",i[0])
        print("ID  :",i[1])
        print("Duration : ",i[2])
        print("Fees : ",i[3])
        print("Instructor : ",i[4])
        print("             ---------                ")
    print()
    c.close()
def check1(n,h):
    c=mydb.cursor()
    con=0
    c.execute(" select course_id from user_details where user_id =%s ",(n,))
    for i in c:
        if i[0]==h:
            con=1
    c.close()
    if con==0:
        return True
    else:
        return False
def newcourse(n):
    c=mydb.cursor()
    course_view1()
    con=0
    h=input("Enter the course id : ")
    c.execute("select * from  course")
    for i in c:
        if i[1]==h:
            con=1
    c.close()
    if con==0:
        print("Try giving valid input!!\n")
        newcourse(n)
    else:    
        t=check1(n,h)
        if t==True:
            c=mydb.cursor()
            c.execute("insert into user_details values (%s,%s)",(h,n,))
            print("Successfully added!!!\n")
            c.execute("commit")
            c.close()
            user_choice(n)
        else:
            print("You have already Taken.")
            user_choice(n)

                 
def user_choice(n):
    print()
    print("------------*****************---------------")
    print("1.     Mycourses")
    print("2.     Add New Courses")
    print("3.     Delete courses")
    print("0.     MainMenu")
    print()
    d=input("Enter the choice :  ")
    if d=="1":
        mycourse(n)
    elif d=="2":
        newcourse(n)
    elif d=="3":
        deletecourse()
    elif d=="0":
        main()
    else:
        user_choice(n)
       
   
def check(name):
    c=mydb.cursor()
    c.execute("select * from user")
    con=0
    for i in c:
        if i[0]==name:
            con=1
    c.close()        
    if con==1:        
        return True  
    else:
        return False
def signup():
    c=mydb.cursor()
    print("*********----------------***********")
    name=input("Enter your name  : ")
    f=check(name)
    if f==True:
        print("User Name already taken take New---")
        signup()
    pas=input("Create a Strong Password :  ")
    phone_no=input("Enter your phone number  :")
    age=input("Enter Your Age  :  ")
    print("**********Your Details:*********")
    print("Name :  ",name,"\nPassword :  ",pas,"\nPhone Number : ",phone_no,"\nAge  :  ",age)
    w=input("press 1 to Confirm: ")
    if(w=="1"):
        c.execute("insert into user values(%s,%s,%s,%s)",(name,pas,phone_no,age))
        print("-------you have successfully Regisered-------")
        print()
        c.execute("commit")
        c.close()
        login()
    else:
        signup()
       
def login():
    c=mydb.cursor()
    print("-------------Login-----------")
    n=input("Enter the UserName  :  ")
    p=input("Enter the Password :  ")
    c.execute("select * from user")
    con=0
    for i in c:
        if n==i[0] and p==i[1]:
            print("--------You have Logined----")
            con=1
    c.close()
    if con==0:
        print("User name  or Password not Found")
    elif con==1:
        user_choice(n)
   
def user():
   
    print("************Welcome to skillMaker*****************")
    print()
    print("1.  -- LOGIN --")
    print("2.  -- SIGNUP --")
    print("0.  --MainMenu--")
    p=input("---Enter the Choices---")
    if p=="1":
        login()
    elif p=="2":
        signup()
    elif p=="0":
        main()
    else:
        user()
   
def main():
    print("Welcome to SkillMaker")
    print("  Option ")
    print("1. Admin")
    print("2. User")
    while(1):
        op=input("Enter Your Option: ")
        if op=="1":
            admin()
            break
        elif op=="2":
            user()
            break
        else:
            print()
            print("*******Invalid choice*******")
            break
            
main()    

