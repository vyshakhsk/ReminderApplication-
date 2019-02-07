from database import *
def CreateReminder(reminder,UserId):
	InsertReminder(reminder,UserId)
def get_data(userId):
	return ViewAllReminder(userId)
def show_data_by_id(id_):
	students = getReminderById(id_)
	if not students:
		print("No data found at roll",id_)
	else:
		print (students)

def ViewReminder(userId):
	remind = get_data(userId)
	for i in remind:
		print(i)
	

def select(userId):
	sp.call('clear',shell=True)
	sel = input("1. Add data\n2.Show Data\n3.Update\n4.Delete\n5.Exit\n\n")

	
	if sel=='1':
		sp.call('clear',shell=True)
		name = input('reminder: ')
		CreateReminder(name,userId)
	elif sel=='2':
		sp.call('clear',shell=True)
		ViewReminder(userId)
		input("\n\npress enter to back:")
	elif sel=='3':
		sp.call('clear',shell=True)
		idt = int(input('Enter Id: '))
		show_data_by_id(userId)
		print()
		reminder = input('New Reminder: ')
		UpdateReminder(idt,reminder,userId)
		input("\n\nYour data has been updated \npress enter to back:")
	elif sel=='4':
		sp.call('clear',shell=True)
		id_ = int(input('Enter Id: '))
		show_data_by_id(userId)
		DeleteReminder(id_)
		input("\n\nYour data has been deleted \npress enter to back:")
	else:
		return 0;
	return 1;

print("REMINDERS ASSIGNMENT\n\n")
CreateUserPassword()
while(1):
        
        print("Are you a new user\n1.Yes\n2.No\n")
        sel1=input()
        print("Enter your name\n")
        a=input()
        f=CheckUser(a)
        if f==1 and sel1=='1':
            print("User Exists!!\n")
        elif f==0 and sel1=='2':
            print("No Such User Exists")
        else:
            t=0
            passw=input("enter password\n")
            if sel1=='1':
                  CreateUsers(a,passw)
                  CreateRemindersTable()
                  t=1
            else:
                  t=CheckPassword(a,passw)
        
            if t==1:
                userId=getUserId(a)
                while(select(userId)):
                    pass
            else:
                  print("Wrong password\n")     
        print("Check another user?? \n1.yes\n2.No")
        y=input()
        if y=='2':
                break

