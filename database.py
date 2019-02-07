import sqlite3
import subprocess as sp


def CreateUserPassword():
        conn = sqlite3.connect('remiderdb.sqlite')
        cursor = conn.cursor()
        query = '''
	    CREATE TABLE IF NOT EXISTS users(
	    	UserId INTEGER PRIMARY KEY AUTOINCREMENT, 
	    	name TEXT,
	        password TEXT
	    )
	'''
        cursor.execute(query)
        conn.commit()
        conn.close()

def CreateUsers(a,passw):
        conn = sqlite3.connect('remiderdb.sqlite')
        cursor = conn.cursor()
        query = '''INSERT INTO users(name,password) VALUES ( ?,? )'''
        cursor.execute(query,(a,passw))
        conn.commit()
        conn.close()

def CheckUser(a):
    conn = sqlite3.connect('remiderdb.sqlite')
    cursor = conn.cursor()
    query = '''
        SELECT name
	FROM users
	''' 
    cursor.execute(query)
    user_pass = cursor.fetchall()
    conn.commit()
    if a in str(user_pass):
        return 1
    else:
        return 0
    

def CheckPassword(a,passw):
        conn = sqlite3.connect('remiderdb.sqlite')
        cursor = conn.cursor()
        query = '''
	    SELECT password
	    FROM users
	    WHERE name="{}"
	''' .format(a)
        cursor.execute(query)
        user_pass = cursor.fetchall()
        conn.commit()
        if str(user_pass[0][0])==str(passw):

                return 1
        else:
                return 0
        
def getUserId(a):
     conn = sqlite3.connect('remiderdb.sqlite')
     cursor = conn.cursor()
     query = '''
	    SELECT UserId
	    FROM users
	    WHERE name="{}"
	''' .format(a)
     cursor.execute(query)
     conn.commit()
     r=cursor.fetchall()[0][0]
     return r
        
   
def CreateRemindersTable():
	conn = sqlite3.connect('remiderdb.sqlite')

	cursor = conn.cursor()

	query = '''
	    CREATE TABLE IF NOT EXISTS reminderTable(
	    	idt INTEGER PRIMARY KEY AUTOINCREMENT, 
	    	reminder TEXT,
	    	UserId INTEGER
	    )
	'''

	cursor.execute(query)

	conn.commit()
	conn.close()

def getReminderById(UserId):
	conn = sqlite3.connect('remiderdb.sqlite')

	cursor = conn.cursor()
	query = '''
	    SELECT idt,reminder
	    FROM reminderTable
	    WHERE UserId={} 
	''' .format(UserId)

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows

def InsertReminder(reminder,UserId):
	conn = sqlite3.connect('remiderdb.sqlite')

	cursor = conn.cursor()

	query = '''
	    INSERT INTO reminderTable(reminder,UserId)
	    	        VALUES(?,?)
	'''

	cursor.execute(query,(reminder,UserId))
	conn.commit()
	conn.close()



def ViewAllReminder(userId):
	conn = sqlite3.connect('remiderdb.sqlite')

	cursor = conn.cursor()

	query = '''
	    SELECT idt, reminder
	    FROM reminderTable
	    WHERE UserId={}
	'''.format(userId)

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows

def DeleteReminder(idt):
	conn = sqlite3.connect('remiderdb.sqlite')

	cursor = conn.cursor()

	query = '''
	    DELETE
	    FROM reminderTable
	    WHERE idt = {}
	''' .format(idt)

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows


def UpdateReminder(idt,reminder,UserId):
	conn = sqlite3.connect('remiderdb.sqlite')

	cursor = conn.cursor()

	query = '''
	    UPDATE reminderTable
	    SET reminder = ?
	    WHERE idt = ?
	'''

	cursor.execute(query,(reminder,idt))

	conn.commit()
	conn.close()


