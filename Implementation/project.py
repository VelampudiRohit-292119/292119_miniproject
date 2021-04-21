import pickle
import os


class student(object):
    def __int__(s):
        s.roll=0
        s.name=""
        s.per=0

    def add_rec(s):
        while(True):
            roll=input("Enter roll no ")
            if(roll.isnumeric()==True):
                s.roll=int(roll)
                break
            else:
                print("only digits")
        while(True):
            name=input("Enter name ")
            if(name.isalpha()==True):
                s.name=name
                break
            else:
                print("Only alphabets please....")
        s.name=s.name.upper()
        while(True):
            s.per=float(input("Enter percentage "))
            if(s.per>100.0):
                print("enter below 100")
            else:
                s.per=round(s.per,2)
                break
                
        
    def disp_rec(s):
        print("roll ",s.roll)
        print("name ",s.name)
        print("per ",s.per)

    def display_rec(s):
        print("%-10s"%s.roll,"%-20s"%s.name,"%-10s"%s.per)
        #print("in display_rec")
        
    def modify_rec(s):
        s.roll=int(input("Enter new roll no "))
        s.name=input("Enter new name ")
        s.name=s.name.upper()
        s.per=float(input("Enter new per "))
    


def write_record():
    try:
        rec=student()
        file=open("stud.dat","ab")
        rec.add_rec()
        pickle.dump(rec,file)
        file.close()
        print("Record added in file")
        input("Press any key to cont ....")
    except:
        pass


def display_all():
    os.system("cls")
    print(40*"=")
    print("\n             Student Records\n")
    print(40*"=")
    try:
        file=open("stud.dat","rb")
        while True:
            rec=pickle.load(file)
            rec.display_rec()
            
            
    except EOFError:
        file.close()
        print(40*"=")
        input("Press any key to cont ....")
    except IOError:
        print("file could not be opened")
        
def search_roll():
    os.system("cls")
    try:
        z=0
        print(40*"=")
        print("Record Searching By Roll No")
        print(40*"=")
        n=int(input("Enter roll no search "))
        file=open("stud.dat","rb")
        while True:
            rec=pickle.load(file)
            #print(rec.roll)
            if(rec.roll==n):
                z=1
                print("\nRecord Found and details are\n")
                rec.disp_rec()
                break
    except EOFError:
        file.close()
        if(z==0):
            print("record is not present")
        
    except IOError:
        print("file could not be opened")
    input("Press any key to cont ....")
        
def search_name():
    os.system("cls")
    try:
        z=0
        n=input("Enter name to search ")
        file=open("stud.dat","rb")
        while True:
            rec=pickle.load(file)
            #print(rec.roll)
            if(rec.name==n.upper()):
                z=1
                rec.disp_rec()
                break
    except EOFError:
        file.close()
        if(z==0):
            print("record is not present")
        
    except IOError:
        print("file could not be opened")   
    input("Press any key to cont ....")    

def modify_roll():
    os.system("cls")
    z=0
    try:
        n=int(input("Enter roll no to modify "))
        file=open("stud.dat","rb")
        temp=open("temp.dat","wb")
        while True:
            rec=pickle.load(file)
            if(rec.roll==n):
                z=1
                print("record found and details are")
                rec.disp_rec()
                print("Enter new data ")
                rec.modify_rec()
                pickle.dump(rec,temp)
                print("Record updated")
            else:
                pickle.dump(rec,temp)

    except EOFError:
        file.close()
        temp.close()
        if(z==0):
            print("Record not found")
    except IOError:
        print("File could not be opened")

    os.remove("stud.dat")
    os.rename("temp.dat","stud.dat")
    input("Press any key to cont ....")

def delete_roll():
    os.system("cls")
    z=0
    try:
        n=int(input("Enter roll no to delete "))
        file=open("stud.dat","rb")
        temp=open("temp.dat","wb")
        while True:
            rec=pickle.load(file)
            if(rec.roll==n):
                z=1
                print("record to delete found and details are")
                rec.disp_rec()
                #pickle.dump(rec,temp)
                #print("Record updated")
            else:
                pickle.dump(rec,temp)

    except EOFError:
        file.close()
        temp.close()
        if(z==0):
            print("Record not found")
    except IOError:
        print("File could not be opened")

    os.remove("stud.dat")
    os.rename("temp.dat","stud.dat")
    input("Press any key to cont ....")



while True:
    os.system("cls")
    print(40*"=")
    print("""            Main Menu
            ---------

           1. Add recod
           2. display all records
           3. search by rollno
           4. search by name
           5. Modify by rollno
           6. delete by rollno
           7. exit
    """)
    print(40*"=")
    ch=int(input("Enter your choice "))
    print(40*"=")
    if(ch==1):
        write_record()
    elif(ch==2):
        display_all()
    elif(ch==3):
        search_roll()
    elif(ch==4):
        search_name()
    elif(ch==5):
        modify_roll()
    elif(ch==6):
        delete_roll()
    elif(ch==7):
        print("End")
        break
    else:
        print("Invalid choice")
