from tabulate import tabulate
import mysql.connector

connection =mysql.connector.connect(host="localhost", user="root", password="1234", database="employee_database")


def insert(empname, dept, age, city):
    res =connection.cursor()
    sql ="insert into employee1 (empname, dept, age,city) values (%s,%s,%s,%s)"
    user =(empname, dept, age, city)
    res.execute(sql, user)
    connection.commit()
    print("Data insert success..")

def update(empname, dept, age, city,id):
    res =connection.cursor()
    sql ="update employee1 set empname=%s, dept=%s, age=%s,city=%s where id=%s"
    user =(empname, dept, age, city,id)
    res.execute(sql, user)
    connection.commit()
    print("Data update success!!")

def delete(id):
    res =connection.cursor()
    sql ="delete from employee1 where id=%s"
    user =(id,)
    res.execute(sql, user)
    connection.commit()
    print("Data delete success")

def select():
    res =connection.cursor()
    sql ="SELECT id, empname, dept, age, city from employee1"
    res.execute(sql)
    result =res.fetchall()
    #print(result)
    print(tabulate(result, headers=['id', 'empname', 'dept', 'age', 'city']))

while True:
    print('1 Insert data')
    print('2 Update data')
    print('3 Delete data')
    print('4 Select data')
    print('5 Exit')

    choice =int(input('Enter your choice: '))
    if choice ==1:
        empname =input('Enter employee name: ')
        dept =input('Enter department name: ')
        age =input('Enter age: ')
        city =input('Enter city: ')
        insert(empname, dept, age, city)
    elif choice==2:
        id =input('Enter the id: ')
        empname =input('Enter employee name: ')
        dept =input('Enter department name: ')
        age =input('Enter age: ')
        city =input('Enter city: ')
        update(empname, dept, age, city, id)
    elif choice ==3:
        id =input("please enter the ID you want to delete: ")
        delete(id)
    elif choice==4:
        select()
    elif choice ==5:
        quit()
    else:
        print('hey fellow, you have entered invalid choice, try again...')