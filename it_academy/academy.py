import csv
from datetime import date
from datetime import timedelta

class ItAcademy:
    course = []
    balance = 0
    enrolled_date = date.today()
    due_date = enrolled_date + timedelta(weeks=12)
    def viewcourse(self):

        with open('course_info.csv', 'r') as course:
            reader = csv.DictReader(course)
            print("Available courses are \n")
            for info in reader:
                self.course.append(info['course name'])
                print(info['course name'],'\t\t',info['course duration'])
        course.close()
        while True:
            print("1. Inquiry")
            print("2. Course Enroll")
            print("3. Exit")

            choice = int(input('Enter your choice: '))
            if choice == 1:
                self.inquiry()
            elif choice == 2:
                self.enroll()
            elif choice == 3:
                exit()
            else:
                print("Invalid choice")

    def inquiry(self):
        name = input("Enter your name ")
        email = input("Enter your email ")
        phone = input("Enter your phone number ")
        courseName = input("Enter your course")
        inquiry = input("Enter your enquiry here ")

        with open('inquiry.csv', 'a+')as inquiry_file:
            writeall = csv.writer(inquiry_file)
            # writeall.writerow(['name', 'email', 'phone', 'course', 'inquiry'])
            writeall.writerows([(name, email, phone, courseName, inquiry)])
        inquiry_file.close()

    def enroll(self):
        self.course_name = input("Enter the course you want to enroll ")
        if self.course_name in self.course:
            self.user()
        else:
            print("Course not available.")
        
    def user(self):
        self.name = input("Enter your name ")
        self.address = input("Enter your address ")
        self.email = input("Your email here ")
        self.phone_number = input("Enter your phone number ")
        self.payment()

    def payment(self):
        balance = int(input("Amount here(20,000 or 10,000 only) "))
        self.balance += balance
        if balance == 20000:
            print("Full paid")
            self.userInfo()
        elif balance == 10000:
            print("Half paid")
            self.userInfo()
        else:
            print("Payment can be done either 20,000 or 10,000")

    def userInfo(self):
        with open('user_info.csv', 'a+')as user_info:
            writer = csv.writer(user_info)
            # writer.writerow(['name', 'adderss', 'email', 'phone', 'course', 'balance paid', 'remaining balance', 'enroll date', 'due date'])
            writer.writerows([(self.name, self.address, self.email, self.phone_number, self.course_name, self.balance, 20000-self.balance, self.enrolled_date, self.due_date )])
            
        user_info.close()
    

    def addcourse(self):
        courseName = input("Enter course name")
        duration = input("Eter duration")

        with open('course_info.csv', 'a+')as course:
            writeall = csv.writer(course)
            # writeall.writerow(['course name', 'course duration'])
            writeall.writerows([(courseName, duration)])
        course.close()

    def displayUserInfo(self):
        with open('user_info.csv', 'r') as userdata:
            reader = csv.DictReader(userdata)
            for userinfo in reader:
                # print(userinfo)
                print(userinfo['name'],'\t',userinfo['adderss'],'\t',userinfo['email'],'\t',userinfo['phone'],'\t',userinfo['course'],'\t',userinfo['balance paid'],'\t',userinfo['remaining balance'],'\t',userinfo['enroll date'],'\t',userinfo['due date'])
        userdata.close()

    def updateUser(self):
        email = input("Enter email ")
        userData = []
        with open('user_info.csv', 'r') as userinfo:
            reader = csv.DictReader(userinfo)
            for data in reader:
                userData.append(data)
            for row in userData:
                if email == row['email']:
                    print(row['name'])
                    row['name'] = input("updated name")
                    print(row['email'])
                    row['email'] = input("updated email")
                    print(row['adderss'])
                    row['adderss'] = input("updated address")
                    print(row['phone'])
                    row['phone'] = input("updated phone")
                    
        userinfo.close()

        with open("user_info.csv", 'w') as edited_data:
            writer = csv.DictWriter(edited_data, fieldnames=['name', 'adderss', 'email', 'phone', 'course', 'balance paid', 'remaining balance', 'enroll date', 'due date'])
            writer.writeheader()
            writer.writerows(userData)
        edited_data.close()            

    def deleteUser(self):
        email = input("Enter email")
        userData = []
        with open("user_info.csv", 'r') as data:
            reader = csv.reader(data)
            for userdata in reader:
                userData.append(userdata)

                for row in userdata:
                    if email == row:
                        userData.remove(userdata)
        data.close()

        with open("user_info.csv", 'w') as data:
            writer = csv.writer(data)
            writer.writerows(userData)
        data.close()

def main():
    itacademy = ItAcademy()
    while True:
        print("1. View course")
        print("2. Users Information")
        print("3. Update user")
        print("4. Delete user")
        choice = int(input("Enter your choice"))
        if choice == 1:
            itacademy.viewcourse()
        elif choice == 2:
            itacademy.displayUserInfo()
        elif choice == 3:
            itacademy.updateUser()
        elif choice == 4:
            itacademy.deleteUser()
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()