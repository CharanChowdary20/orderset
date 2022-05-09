def person(**data):
    for A, B in data.items():
        if A == 'firstname':
            print(A, ' :', B)
        elif A == 'lastname':
            print(A, '  :', B)
        elif A == 'age':
            print(A, '       :', B)
        else:
            print (A, '  :',B)

e = 1
while e != '0':
    firstname = input("Enter your First Name:")
    lastname = input("Entre your Last Name:")
    age = input("Enter your age:")
    mobile = input("Enter your mobile no:")
    print('')
    person(firstname=firstname, lastname=lastname, age=age, mobileno=mobile)
    e = input("Enter 0 exit or any key to Continue")